def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:
    # check if tanks array bigger than map
    if h2 > h1 or w2 > w1:
        return False

    map_list = s1.split(' ')
    tanks_list = s2.split(' ')
    element_to_match = tanks_list[0][0]

    for row in range(h1 - h2 + 1):
        for col in range(w1 - w2 + 1):
            if map_list[row][col] == element_to_match:
                if is_matching(tanks_list, map_list, row, col, h2, w2):
                    return True
    return False


def is_matching(tanks_list: list[str], map_list: list[str],
                row: int, col: int, h2: int, w2: int) -> bool:

    bool_list = []
    for tank_row in range(h2):
        bool_list.append(
            tanks_list[tank_row] == map_list[row + tank_row][col:w2 + col]
        )
    return all(bool_list)
