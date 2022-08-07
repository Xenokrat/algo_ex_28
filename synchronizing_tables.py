def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    salary.sort()  # sorting list of salaries
    zipped_ids_salary = list(zip(ids, salary))

    # sort list of pairs ids <--> salary by ids order
    sorted_tuples = sorted(zipped_ids_salary, key=lambda x: x[0])
    res = [x for _, x in sorted_tuples]  # extract salaries from list of tuples
    return res
