# 切换地图
def change_map(client, map_name):
    client.load_world(map_name)

# 获取可用地图列表
def get_available_maps(client):
    return client.get_available_maps()