def ShopOLAP(n: int, items: list[str]) -> list[str]:
    items_dict = make_dict(items)
    sorted_items = sort_items(items_dict)

    # back to list of strings
    res = []
    for pair in sorted_items:
        product = pair[0]
        count = str(pair[1])
        product_count = product + ' ' + count
        res.append(product_count)
    return res


def make_dict(items):
    item_dict = {}
    for item in items:
        pair = item.split(' ')

        product = pair[0]
        count = int(pair[1])

        if product not in item_dict:
            item_dict[product] = count
        else:
            item_dict[product] += count
    return item_dict


def sort_items(items_dict: dict) -> list[tuple]:
    items_tuple = [(k, v) for k, v in items_dict.items()]
    sorted_list = sorted(
        items_tuple,
        key=lambda x: (-x[1], x[0])
    )
    return sorted_list
