def Unmanned(length: int, n: int, track: list[list[int]]) -> int:
    awaited = 0  # time spend on red

    # process all traffic lights in list
    for traffic_light in track:

        # if the light is further than length, should not process it
        if traffic_light[0] >= length:
            continue

        des_time = traffic_light[0] + awaited
        red_time = traffic_light[1]
        green_time = traffic_light[2]

        # calculate full light cycle and add to awaited
        tl_cycle = red_time + green_time
        residual = des_time % tl_cycle
        if residual < red_time:
            awaited += red_time - residual

    total_time = length + awaited

    return total_time
