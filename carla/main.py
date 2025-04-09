import carla
from utils.map import change_map

client = carla.Client("192.168.31.125", 2000)
client.set_timeout(10.0)
change_map(client, "Town01")
world = client.get_world()