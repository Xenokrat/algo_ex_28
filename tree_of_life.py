def TreeOfLife(h: int, w: int, n: int, tree: list[str]) -> list[str]:
    parsed_tree = parse_string(tree)

    # main loop
    for year in range(0, n):
        if year % 2 == 0:
            parsed_tree = even_year(parsed_tree, h, w)
        else:
            parsed_tree = odd_year(parsed_tree, h, w)

    parsed_to_str_tree = parse_string_back(parsed_tree)
    return parsed_to_str_tree


def even_year(parsed_tree: list[list[int]], h: int, w: int) -> list[list[int]]:
    # create new branches, increase age of existing branches
    for row in range(h):
        for col in range(w):
            parsed_tree[row][col] += 1
    return parsed_tree


def odd_year(parsed_tree: list[list[int]], h: int, w: int) -> list[list[int]]:
    # branches become older
    new_parsed_tree = even_year(parsed_tree, h, w)

    branches_to_del = set()
    for row in range(h):
        for col in range(w):
            if new_parsed_tree[row][col] > 2:
                branches_to_del.add((row, col))

    branches_to_del_copy = branches_to_del.copy()
    for branch in branches_to_del_copy:
        # add upper
        if branch[0] > 0:
            branches_to_del.add((branch[0] - 1, branch[1]))

        # add bottom
        if branch[0] < h - 1:
            branches_to_del.add((branch[0] + 1, branch[1]))

        # add left
        if branch[1] > 0:
            branches_to_del.add((branch[0], branch[1] - 1))

        # add right
        if branch[1] < w - 1:
            branches_to_del.add((branch[0], branch[1] + 1))

    for branch in branches_to_del:
        row = branch[0]
        col = branch[1]
        new_parsed_tree[row][col] = 0

    return new_parsed_tree


def parse_string(tree: list[str]) -> list[list[int]]:
    res = []
    for symbol_line in tree:
        int_line = [0 if symbol == '.' else 1 for symbol in symbol_line]
        res.append(int_line)

    return res


def parse_string_back(tree: list[list[int]]) -> list[str]:
    res = []
    for int_line in tree:
        symbols_line = ['.' if num == 0 else '+' for num in int_line]
        string_line = ''.join(symbols_line)
        res.append(string_line)

    return res
