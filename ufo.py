def UFO(n: int, data: list[int], octal: bool) -> list[int]:
    if octal:
        base = 8
    else:
        base = 16

    res = []
    for num in data:
        ten_based = 0
        trans_num = str(num)[::-1]

        for ind, digit in enumerate(trans_num):
            ten_based += int(digit) * (base ** ind)

        res.append(ten_based)

    return res
