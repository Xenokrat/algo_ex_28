def BigMinus(s1: str, s2: str) -> str:
    len_s1 = len(s1)
    len_s2 = len(s2)

    # 1. Calculate which number is bigger
    if s1 == s2:
        return '0'

    first_num, second_num = s1, s2
    if len_s1 < len_s2:
        first_num, second_num = s2, s1

    elif len_s1 == len_s2:
        counter = 0
        while counter < len_s1:
            if int(s1[counter]) > int(s2[counter]):
                first_num, second_num = s1, s2
                break
            if int(s1[counter]) < int(s2[counter]):
                first_num, second_num = s2, s1
                break
            counter += 1

    # 2. Calculate the difference: "first_num" - "second_num"
    min_number_length = min(len_s1, len_s2)
    max_number_length = max(len_s1, len_s2)
    next_num_minus = 0
    res_reversed = ''

    for ind in range(1, min_number_length + 1):
        num_s1 = int(first_num[-ind])
        num_s2 = int(second_num[-ind])

        if num_s1 - num_s2 - next_num_minus < 0:
            diff = (num_s1 + 10) - num_s2 - next_num_minus
            next_num_minus = 1
        else:
            diff = num_s1 - num_s2 - next_num_minus
            next_num_minus = 0
        res_reversed += str(diff)

    for ind in range(min_number_length + 1, max_number_length + 1):
        num_s1 = int(first_num[-ind])
        if num_s1 - next_num_minus < 0:
            diff = 9
            next_num_minus = 1
        else:
            diff = num_s1 - next_num_minus
            next_num_minus = 0

        res_reversed += str(diff)

    # 3. Delete unnecessary nulls
    res_with_nulls = res_reversed[::-1]
    null_counter = 0
    while null_counter < len(res_with_nulls):
        if res_with_nulls[null_counter] == '0':
            null_counter += 1
        else:
            break
    res = res_with_nulls[null_counter:]

    return res
