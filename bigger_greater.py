def BiggerGreater(_input: str) -> str:

    n = len(_input)
    input_list = list(_input)

    suffix = None
    prefix = None
    first_pivot = ''

    # identify the longest suffix that is non-increasing
    for ind in range(n - 1, 0, -1):
        right = input_list[ind]
        left = input_list[ind - 1]
        if left < right:
            suffix = input_list[ind:]
            prefix = input_list[:ind - 1]  # not include first_pivot
            first_pivot = left
            break

    # no suffix - no any greater value
    if not suffix:
        return ''

    # find first from end element in suffix that bigger than pivot
    second_pivot = 0
    len_suffix = len(suffix)
    for j in range(len_suffix - 1, 0, -1):
        if suffix[j] > first_pivot:
            second_pivot = j
            break

    # swap them
    suffix[second_pivot], first_pivot = first_pivot, suffix[second_pivot]

    # reverse new suffix to make the least possible value
    new_suffix = suffix[::-1]

    prefix_str = ''.join(prefix)
    suffix_str = ''.join(new_suffix)
    res = prefix_str + first_pivot + suffix_str

    return res
