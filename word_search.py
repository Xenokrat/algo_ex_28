def WordSearch(length: int, s: str, subs: str) -> list[int]:

    words_list = s.split(' ')
    words_lines = []

    while words_list:
        line = []
        current_length = 0

        while words_list:
            word = words_list.pop(0)

            # if word longer than length
            if len(word) > length and len(line) < 1:
                line = [word[:length], '\n']
                words_list = [word[length:]] + words_list
                break

            current_length += len(word)

            if current_length <= length:
                line.append(word)
                if len(line) > 1:
                    current_length += 1  # adding "space"
            else:
                line.append('\n')
                words_list = [word] + words_list
                break

        words_lines.append(line)

    # res = "".join([" ".join(line) for line in words_lines])  # this will return align text
    res = [1 if subs in worlds_line else 0 for worlds_line in words_lines]
    return res

