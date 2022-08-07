def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    salary.sort()
    zipped_ids_salary = list(zip(ids, salary))
    sorted_tuples = sorted(zipped_ids_salary, key=lambda x: x[0])
    res = [x for _, x in sorted_tuples]
    return res
