def odometer(oksana: list[int]) -> int:
    distance = 0
    time_start = 0
    points = len(oksana) - 1

    for i in range(0, points, 2):
        time_delta = oksana[i + 1] - time_start
        time_start = oksana[i + 1]
        distance += oksana[i] * time_delta

    return distance
