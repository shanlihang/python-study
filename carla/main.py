import time
import carla
import logging

import numpy as np
from utils.map import change_map
from utils.point import draw_spawn_points
from camera.semantic_segmentation import print_type_count

# 启动 CARLA 客户端并处理连接问题
try:
    client = carla.Client("192.168.31.125", 2000)
    client.set_timeout(10.0)
    world = client.get_world()
except Exception as e:
    logging.error(f"连接 CARLA 服务失败: {e}")
    exit(1)

try:
    # change_map(client, "Town04")
    # draw_spawn_points(world)

    blueprint_library = world.get_blueprint_library()

    spawn_points = world.get_map().get_spawn_points()
    camera_location = spawn_points[207].location
    camera_location.z += 15
    camera_location.x += 5
    camera_location.y += 5
    camera_rotation = carla.Rotation(pitch=-35, yaw=0, roll=0)

    camera_bp = blueprint_library.find('sensor.camera.semantic_segmentation')
    camera_bp.set_attribute("image_size_x", "800")
    camera_bp.set_attribute("image_size_y", "600")
    camera_bp.set_attribute("fov", "90")

    camera_transform = carla.Transform(camera_location, camera_rotation)
    camera = world.spawn_actor(camera_bp, camera_transform)

    if camera is None:
        raise RuntimeError("摄像头生成失败。")

    camera.listen(lambda image: print_type_count(image))

    print("车辆与摄像头已成功启动，正在采集图像...")
    time.sleep(300)

except Exception as e:
    logging.error(f"执行过程中出错: {e}")

finally:
    if 'camera' in locals():
        camera.destroy()
    print("资源释放完毕")
