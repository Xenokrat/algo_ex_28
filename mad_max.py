def MadMax(N: int, Tele: list[int]) -> list[int]:
    Tele.sort()
    mid = N // 2
    counter = 1
    # reverse the second part of the list
    for ind in range(mid, mid + (mid // 2 + 1)):  # mid + (mid // 2 + 1) need to swap only from 1/2 to 3/4 part
        Tele[ind], Tele[N - counter] = Tele[N - counter], Tele[ind]
        counter += 1

    return Tele

