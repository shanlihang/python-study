import os
import cv2
import numpy as np
from camera.data import id_to_label, id_to_color


def print_type_count(image):
    array = np.frombuffer(image.raw_data, dtype=np.uint8)
    array = array.reshape((image.height, image.width, 4))
    seg_ids = array[:, :, 2]

    # 定义你关心的目标类别
    target_classes = {
        "car": [14, 15, 16, 17],
        "Motorcycle": [18],
        "Bicycle": [13, 19]
    }

    detection_summary = {}
    for name, ids in target_classes.items():
        mask = np.isin(seg_ids, ids).astype(np.uint8)
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)

        # 忽略背景，过滤面积过小的目标
        min_area = 15
        count = sum(1 for stat in stats[1:] if stat[cv2.CC_STAT_AREA] >= min_area)
        detection_summary[name] = count

    # 生成彩色图像
    color_image = np.zeros((image.height, image.width, 3), dtype=np.uint8)
    for seg_class, color in id_to_color.items():
        color_image[seg_ids == seg_class] = color

    # 准备要写在图像上的文字内容
    lines = [f"{name}------{count}" for name, count in detection_summary.items()]

    # 设置文字样式
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.6
    color = (255, 255, 255)  # 白色文字
    thickness = 2
    line_height = 25
    margin = 10
    start_x = image.width - 200
    start_y = margin + line_height

    # 写每一行文字到图像右上角
    for i, line in enumerate(lines):
        position = (start_x, start_y + i * line_height)
        cv2.putText(color_image, line, position, font, font_scale, color, thickness, cv2.LINE_AA)

    # 保存图像
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, '%08d.jpg' % image.frame)
    cv2.imwrite(filename, color_image)