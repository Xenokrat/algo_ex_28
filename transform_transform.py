def TransformTransform(a: list[int], n: int) -> bool:
    res1 = transform(a, n)
    res2 = transform(res1, len(res1))
    sum_res = sum(res2)
    return sum_res % 2 == 0


def transform(a: list[int], n: int) -> list[int]:
    b = []
    for i in range(n):
        for j in range(n - i):
            k = i + j
            subarray = a[j:k + 1]
            b.append(max(subarray))

    return b
