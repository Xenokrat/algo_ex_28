from collections import deque


def MatrixTurn(
        matrix: list[str],
        rows: int,
        cols: int,
        t: int) -> None:

    assert min(rows, cols) % 2 == 0

    matrix_copy = [list(x) for x in matrix]
    circle_indexes = make_circle_indexes(rows, cols)
    rotated_indexes = shift_circle(circle_indexes, t)
    rotate_circle(matrix_copy)


def make_circle_indexes(rows: int, cols: int) -> list[tuple]:
    upper = [(0, col) for col in range(cols)]
    right = [(row, cols - 1) for row in range(1, rows)]
    bottom = [(rows - 1, col) for col in range(cols - 2, -1, -1)]
    left = [(row, 0) for row in range(rows - 2, 0, -1)]
    circle = upper + right + bottom + left
    return circle


def shift_circle(circle: list[tuple], t: int) -> list[tuple]:
    deque_circle = deque(circle)
    deque_circle.rotate(t)
    return list(deque_circle)


def rotate_circle(matrix: list[str],
                  rotated_indexes: list[tuple],
                  rows: int,
                  cols: int) -> None:
    empty_matrix = [[0] * cols for _ in range(rows)]
    for pos in rotated_indexes:
        pass
