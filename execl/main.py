import pandas as pd
from pymongo import MongoClient
import sys

def connect_mongodb():
    """连接到 MongoDB 数据库"""
    try:
        # 连接到 MongoDB 服务器
        client = MongoClient("mongodb://localhost:27017/")
        # 获取或创建数据库
        db = client["resource"]
        # 获取或创建集合
        collection = db["school"]
        print("MongoDB 连接成功")
        return client, collection
    except Exception as e:
        print(f"MongoDB 连接失败: {e}")
        sys.exit(1)

def main():
    # 连接 MongoDB
    client, collection = connect_mongodb()
    
    try:
        # 读取 Excel 文件
        df = pd.read_excel("W020250729615142156867.xls", skiprows=2, nrows=67)
        
        # 遍历数据并存储到 MongoDB
        records_inserted = 0
        for index, row in df.iterrows():
            # 创建文档
            school_doc = {
                "name": row["学校名称"],
                "code": row["学校标识码"],
                "department": row["主管部门"],
                "area":row["所在地"],
                "category":"普通高等学校",
                "level":row["办学层次"],
                "type": row["备注"] if not pd.isna(row["备注"]) else "公办"
            }
            
            # 插入文档到集合中
            result = collection.insert_one(school_doc)
            records_inserted += 1
            
            # 打印插入的数据
            print(f"已插入: {row['学校名称']}, ID: {result.inserted_id}")
        
        print(f"成功插入 {records_inserted} 条记录到 MongoDB")
    
    except Exception as e:
        print(f"处理数据时出错: {e}")
    
    finally:
        # 关闭 MongoDB 连接
        client.close()
        print("MongoDB 连接已关闭")


if __name__ == "__main__":
    main()
