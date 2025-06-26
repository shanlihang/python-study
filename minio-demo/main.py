from minio import Minio
from minio_utils import create_bucket,delete_bucket

def main():
    client = Minio(
        endpoint="localhost:9000",               # MinIO 服务地址
        access_key="minioadmin",                # Access Key
        secret_key="minioadmin",                # Secret Key
        secure=False                            # http 设为 False；如果是 https，设为 True
    )
    # 查询桶
    objects = client.list_objects("demo001", recursive=True)
    for obj in objects:
        print(obj.object_name, obj.size)

    # 创建桶
    res = create_bucket(client=client,name="demo002")
    if(res):
        print("创建成功")
    else:
        print("创建失败")

    # 删除桶
    res = delete_bucket(client=client,name="demo002")
    if(res):
        print("删除成功")
    else:
       print("删除失败")

if __name__ == "__main__":
    main()
