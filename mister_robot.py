def MisterRobot(n: int, data: list[int]) -> bool:
    # if count of inversions (a[i] > a[j] and i < j) is odd
    # cannot sort this
    inversions = count_inversions(n, data)
    res = inversions % 2 == 0
    return res


def count_inversions(n: int, data: list[int]) -> int:
    m = 1
    inversions = 0
    for ind1 in range(n - 1):
        for ind2 in range(m, n):
            first = data[ind1]
            second = data[ind2]
            if first > second:
                inversions += 1
        m += 1
    return inversions
