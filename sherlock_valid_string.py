def SherlockValidString(s: str) -> bool:
    char_map = make_char_map(s)
    char_values = list(char_map.values())

    max1 = max(char_values)
    max2 = None
    max1_count = 0
    max2_count = 0

    for val in char_values:
        if val == max1:
            max1_count += 1
        elif val < max1 and not max2:
            max2 = val
            max2_count += 1
        elif val == max2:
            max2_count += 1
        else:  # false if there are more than 2 different value counts
            return False

    # Valid passwords

    # 1. Same number of value count
    if not max2:
        return True

    # 2. 2 values, can delete one char to make them equal
    # xxxyyyzz
    elif max2_count == 1 and max2 == 1:
        return True

    elif max1 - max2 == 1 and (max1_count == 1):
        return True

    else:
        return False


def make_char_map(s) -> dict:
    char_map = {}
    for char in s:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1

    return char_map
