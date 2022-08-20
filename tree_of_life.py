def TreeOfLife(h: int, w: int, n: int, tree: list[str]) -> list[str]:
    # main loop

    parsed_tree = parse_string(tree)
    for year in range(1, n):
        if year % 2 == 1:
            pass


def even_year(parsed_tree: list[list[int]], h: int, w: int) -> list[list[int]]:
    # create new branches, increase age of existing branches
    for row in range(h):
        for col in range(w):
            parsed_tree[row][col] += 1
    return parsed_tree


def odd_year(parsed_tree: list[list[int]], h: int, w: int) -> list[list[int]]:
    # branches become older
    new_parsed_tree = even_year(parsed_tree)

    branches_to_del = set()
    for row in range(h):
        for col in range(w):
            if new_parsed_tree[row][col] > 2:
                branches_to_del.add((row, col))

    for branch in branches_to_del.copy():
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


def parse_string(tree: list[str]) -> list[list[int]]:
    res = []
    for symbol_line in tree:
        int_line = [0 if symbol == '.' else 1 for symbol in symbol_line]
        res.append(int_line)

    return res


def parse_string_back(tree: list[list[int]]) -> list[int]:
    res = []
    for int_line in tree:
        symbols_line = ['.' if num == 0 else '+' for num in int_line]
        string_line = ''.join(symbols_line)
        res.append(string_line)

    return res
