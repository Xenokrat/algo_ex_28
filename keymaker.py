def Keymaker(k: int) -> str:
    doors = ['0'] * k
    for i in range(1, k + 1):
        step = i
        while step <= k:
            if doors[step - 1] == '0':
                doors[step - 1] = '1'
            else:
                doors[step - 1] = '0'
            step += i
    res = ''.join(doors)
    return res
