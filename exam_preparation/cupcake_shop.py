from collections import deque


def stock_availability(*args):
    products = deque(args)
    inventory_list = deque(products.popleft())
    command = products.popleft()

    if command == 'delivery':
        inventory_list += products

    if command == 'sell':
        if not products:
            inventory_list.popleft()

        while products:
            if type(products[0]) == int:
                for i in range(products.popleft()):
                    inventory_list.popleft()

            elif products[0] not in inventory_list:
                products.popleft()

            elif products[0] in inventory_list:
                while products[0] in inventory_list:
                    inventory_list.remove(products[0])
                products.popleft()
    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


