def white_walkers(village: str) -> bool:
    first_digit = None
    second_digit = None
    counter = 0
    status = True
    for char in village:
        if char.isdigit():
            if not first_digit:
                first_digit = int(char)

            elif not second_digit:
                second_digit = int(char)
                sum_ = first_digit + second_digit
                if sum_ == 10 and counter != 3:
                    return False
                first_digit, second_digit = second_digit, None
                status = True
            counter = 0

        if char == '=':
            counter += 1
            status = False

    return status
