def squirrel(N: int) -> int:
    res = 1

    for num in range(2, N + 1):
        res *= num
        while res % 10 == 0:
            res //= 10

    while res >= 10:
        res //= 10

    return res
