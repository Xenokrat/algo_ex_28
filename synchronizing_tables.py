def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:

    # find the correct relative order for employees
    ids_sorted = sorted(ids)
    correct_order = [ids_sorted.index(i) for i in ids]

    # rearrange all salaries according to correct order
    salary.sort()
    res = []
    for pos in correct_order:
        res.append(salary[pos])

    return res

