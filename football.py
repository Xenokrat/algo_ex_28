def Football(f: list[int], n: int) -> bool:
    can_reverse = can_reverse_sort(f, n)
    can_swap = can_swap_sort(f, n)
    return any((can_reverse, can_swap))


# find if we can sort by reversing subarray
def can_reverse_sort(f: list[int], n: int) -> bool:
    subarray_start = None

    # find where reversed subarray starts
    for ind in range(n - 1):
        if f[ind] > f[ind + 1]:
            subarray_start = ind
            break

    # if already sorted
    if subarray_start is None:
        return True

    # find reversed subarray endpoint
    ind = subarray_start
    while f[ind] > f[ind + 1] and ind < n:
        ind += 1
        if ind == n - 1:
            break

    subarray_end = ind

    # check if list will be sorted after reversing subarray
    # all conditions should be true
    if subarray_start > 0:
        condition1 = f[subarray_start - 1] < f[subarray_end]
    else:
        condition1 = True

    if subarray_end < n - 1:
        condition2 = f[subarray_start] < f[subarray_end + 1]
    else:
        condition2 = True

    # if there is other inversed numbers
    while subarray_end < n - 1:
        if f[subarray_end] > f[subarray_end + 1]:
            return False
        subarray_end += 1

    return all([condition1, condition2])


def can_swap_sort(f: list[int], n: int) -> bool:
    f_copy = f.copy()
    f_copy.sort()

    counter = 0
    for ind in range(n):
        if f[ind] != f_copy[ind]:
            counter += 1

    res = (counter == 0) or (counter == 2)
    return res
