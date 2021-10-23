def shopping_list(arg, **kwargs):
    budget = arg
    products = kwargs  # key = product, value = (price, quantity)
    basket = {}
    result = ''

    if budget < 100:
        return "You do not have enough budget.\n"

    for product, info in products.items():
        if len(basket) == 5:
            return result

        price = info[0] * info[1]
        if budget < price:
            continue

        basket[product] = price
        budget -= price

        line = f'You bought {product} for {price:.2f} leva.\n'
        result += line

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))