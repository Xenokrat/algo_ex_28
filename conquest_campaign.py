def ConquestCampaign(row: int, col: int, L: int, battalion: list[int]) -> int:
    captured_cells = set()
    cells_to_check_next = set()
    battalion_size = L * 2
    days = 1

    # assert position
    for i in range(0, battalion_size, 2):
        captured_cells.add((battalion[i], battalion[i + 1]))

    cells_to_check_current = captured_cells.copy()

    empty_cells = row * col - len(cells_to_check_current)

    # do until there are no empty cells
    while empty_cells > 0:

        for pos in cells_to_check_current:

            row_pos, col_pos = pos
            # adding upper
            if row_pos > 1 and (row_pos - 1, col_pos) not in captured_cells:
                captured_cells.add((row_pos - 1, col_pos))
                cells_to_check_next.add((row_pos - 1, col_pos))
                empty_cells -= 1

            # adding down
            if row_pos <= row - 1 and (row_pos + 1, col_pos) not in captured_cells:
                captured_cells.add((row_pos + 1, col_pos))
                cells_to_check_next.add((row_pos + 1, col_pos))
                empty_cells -= 1

            # adding left
            if col_pos > 1 and (row_pos, col_pos - 1) not in captured_cells:
                captured_cells.add((row_pos, col_pos - 1))
                cells_to_check_next.add((row_pos, col_pos - 1))
                empty_cells -= 1

            # adding right
            if col_pos <= col - 1 and (row_pos, col_pos + 1) not in captured_cells:
                captured_cells.add((row_pos, col_pos + 1))
                cells_to_check_next.add((row_pos, col_pos + 1))
                empty_cells -= 1

        cells_to_check_current = cells_to_check_next.copy()
        cells_to_check_next = set()
        days += 1

    return days
