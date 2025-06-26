from minio.error import S3Error

def create_bucket(client,name:str) -> bool:
    if not client.bucket_exists(name):
        client.make_bucket(name)
        return True
    else:
        return False

def delete_bucket(client,name:str) -> bool:
    try:
        client.remove_bucket(name)
        print(f"[INFO] 桶已删除：{name}")
        return True
    except S3Error as e:
        print(f"[ERROR] 删除桶失败：{name}，原因：{e}")
        return False