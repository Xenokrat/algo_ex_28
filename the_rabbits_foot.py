def TheRabbitsFoot(s: str, encode: bool) -> str:

    # encoding path
    if encode:

        no_spaces_s = s.replace(" ", "")
        length = len(no_spaces_s)
        length_sqrt = length ** 0.5
        matrix_rows = int(length_sqrt)
        matrix_cols = -int(-length_sqrt // 1)  # round up hack

        # if matrix size is not enough
        while matrix_rows * matrix_cols < length:
            matrix_rows += 1

        s_matrix = []
        counter_start = 0

        # make base matrix
        for row in range(matrix_rows):
            counter_end = counter_start + matrix_cols
            row_line = no_spaces_s[counter_start:counter_end]
            s_matrix.append(row_line)
            counter_start += matrix_cols

        s_t_matrix = []

        # transpose matrix to encode
        for col in range(matrix_cols):
            line = ''
            for row in range(matrix_rows - 1):  # leave the last row for later
                line += s_matrix[row][col]
            s_t_matrix.append(line)

        # adding characters from last row
        word_count = 0
        for char in s_matrix[-1]:
            s_t_matrix[word_count] += char
            word_count += 1

        res = " ".join(s_t_matrix)

    # decoding path
    else:
        res = ''
        split_s = s.split(' ')
        max_length = len(split_s[0]) - 1
        pointer = 0

        # take every "pointer" char in every word and add to res
        while pointer < max_length:
            for word in split_s:
                res += word[pointer]
            pointer += 1

        # handle the last chars
        for word in split_s:
            if len(word) == max_length + 1:
                res += word[-1]

    return res
