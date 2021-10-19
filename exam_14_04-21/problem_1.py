from collections import deque

orders = deque([int(x) for x in input().split(', ') if int(x) in range(1, 11)])
employees = deque([int(x) for x in input().split(', ')])
total_pizzas = 0
all_orders_done = False
no_more_employees = False

while True:
    if not orders:
        all_orders_done = True
        break

    if not employees:
        no_more_employees = True
        break

    if orders[0] <= employees[-1]:
        total_pizzas += orders[0]
        orders.popleft()
        employees.pop()

    else:
        total_pizzas += employees[-1]
        orders[0] -= employees.pop()

orders = list(map(lambda x: str(x), orders))
employees = list(map(lambda x: str(x), employees))

if all_orders_done:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(employees)}')

else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(orders)}')




