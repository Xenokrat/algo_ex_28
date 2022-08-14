def LineAnalysis(line: str) -> bool:

    # calculate template
    counter = 1 
    while counter < len(line):
        if line[counter] == '*':
            break
        counter += 1

    template = line[:counter]
    template_len = len(template)
    parts = len(line) // template_len

    if (len(line) - 1) % template_len != 0:
        return False

    bool_arr = [line[-1] == '*']
    for part in range(parts):
        start = template_len * part
        end = start + template_len
        bool_arr.append(line[start:end] == template)

    return all(bool_arr)
