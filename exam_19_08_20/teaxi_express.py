from collections import deque

customers = deque(int(x) for x in input().split(', '))
cars = [int(x) for x in input().split(', ')]

time_driving = 0

while customers:
    if not cars:
        break
    current_customer = customers[0]
    current_car = cars[-1]

    if current_car >= current_customer:
        time_driving += current_customer
        customers.popleft()
        cars.pop()

    else:
        cars.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {time_driving} minutes")

else:
    customers = [str(x) for x in customers]
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(customers)}")