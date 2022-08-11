def Unmanned(length: int, n: int, track: list[list[int]]) -> int:
    awaited = 0
    for traffic_light in track:
        des_time = traffic_light[0] + awaited
        red_time = traffic_light[1]
        green_time = traffic_light[2]
        tl_cycle = red_time + green_time
        residual = des_time % tl_cycle
        if residual < red_time:
            awaited += red_time - residual

    total_time = length + awaited

    return total_time
