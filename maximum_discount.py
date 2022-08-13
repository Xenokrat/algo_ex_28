def MaximumDiscount(n: int, price: list[int]) -> int:
    sorted_price = sorted(price, reverse=True)
    set_of_buys = n // 3
    max_discount = 0
    for buy in range(set_of_buys):
        cheap_item_pos = buy * 3 + 2
        max_discount += sorted_price[cheap_item_pos]

    return max_discount
