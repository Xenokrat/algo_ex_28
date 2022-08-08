def PatternUnlock(N: int, hits: list[int]) -> str:
    close = 1
    diagonal = 2 ** (1/2)

    # # hard coding panel
    # 6  1  9
    # 5  2  8
    # 4  3  7
    panel = {
        1: {
            2: close, 6: close, 9: close,
            5: diagonal, 8: diagonal,
        },
        2: {
            1: close, 5: close, 8: close, 3: close,
            6: diagonal, 9: diagonal, 4: diagonal, 7: diagonal,
        },
        3: {
            4: close, 2: close, 7: close,
            5: diagonal, 8: diagonal,
        },
        4: {
            5: close, 3: close,
            2: diagonal,
        },
        5: {
            6: close, 2: close, 4: close,
            1: diagonal, 3: diagonal,
        },
        6: {
            1: close, 5: close,
            2: diagonal,
        },
        7: {
            8: close, 3: close,
            2: diagonal,
        },
        8: {
            9: close, 2: close, 7: close,
            1: diagonal, 3: diagonal,
        },
        9: {
            1: close, 8: close,
            2: diagonal
        },
    }
    # calculating sum dist
    sum_dist = 0
    for i in range(N - 1):
        number = hits[i]
        next_number = hits[i + 1]
        sum_dist += panel[number][next_number]

    sum_dist_rounded = round(sum_dist, 5)
    sum_dist_str = str(sum_dist_rounded).replace("0", "").replace(".", "")

    return sum_dist_str
