import carla

# 高亮标记所有可生成点 - 汽车
def draw_spawn_points(world,rgb=(255, 0, 0),debug_type="string"):
    """ 在地图上标记所有可生成点，并高亮 204 号点位 """
    spawn_points = world.get_map().get_spawn_points()
    debug = world.debug

    for i, spawn_point in enumerate(spawn_points):
        location = spawn_point.location
        color = carla.Color(*rgb)

        if debug_type == "string":
            # 普通生成点文字标记
            debug.draw_string(location, str(i), draw_shadow=False, color=color, life_time=100.0, persistent_lines=True)
        elif debug_type == "point":
            # 普通生成点方块标记
            debug.draw_point(location, size=0.3, color=color, life_time=100.0, persistent_lines=True)
        else:
            print("debug_type error")
            return
