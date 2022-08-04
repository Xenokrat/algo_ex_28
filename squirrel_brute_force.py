def squirrel_brute_force(N: int) -> int:
    factorial = 1
    for num in range(2, N + 1):
        factorial *= num

    return int(str(factorial)[0])
