from collections import deque


def MatrixTurn(
        matrix: list[str],
        rows: int,
        cols: int,
        t: int) -> None:

    matrix_copy = [list(x) for x in matrix]

    # assert min(rows, cols) % 2 == 0
    circles_count = min(rows, cols) // 2

    circles_list = []
    for shift in range(circles_count):
        new_rows = rows - shift * 2
        new_cols = cols - shift * 2
        circle = make_circle_indexes(matrix_copy,
                                     new_rows, new_cols, shift)
        rotated_circle = rotate_circle(circle, t)
        circles_list.extend(
            rotated_circle
        )

    # write things back in empty matrix
    for ind_value in circles_list:
        row_ = ind_value[0][0]
        col_ = ind_value[0][1]
        val = ind_value[1]
        matrix_copy[row_][col_] = val

    matrix_copy_str = [''.join(i) for i in matrix_copy]

    for row in range(rows):
        matrix[row] = matrix_copy_str[row]


def make_circle_indexes(matrix: list[list[str]],
                        rows: int, cols: int, shift: int) -> list[list]:
    # ((row, column), value)
    upper = [
        [(0 + shift, col + shift),
         matrix[0 + shift][col + shift]]
        for col in range(cols)
    ]

    right = [
        [(row + shift, cols - 1 + shift),
         matrix[row + shift][cols - 1 + shift]]
        for row in range(1, rows)
    ]

    bottom = [
        [(rows - 1 + shift, col + shift),
         matrix[rows - 1 + shift][col + shift]]
        for col in range(cols - 2, -1, -1)
    ]

    left = [
        [(row + shift, 0 + shift),
         matrix[row + shift][0 + shift]]
        for row in range(rows - 2, 0, -1)
    ]

    circle = upper + right + bottom + left

    return circle


def rotate_circle(circle: list[list], t: int) -> list[list]:
    new_circle = circle.copy()
    value_circle = [val[1] for val in new_circle]
    deque_circle = deque(value_circle)
    deque_circle.rotate(t)
    for ind, val in enumerate(new_circle):
        new_circle[ind][1] = deque_circle[ind]

    return new_circle
