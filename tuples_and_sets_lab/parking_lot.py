n = int(input())
parked_cars = set()
for _ in range(n):
    action, car = input().split(', ')
    if action == 'IN':
        parked_cars.add(car)
    elif action == 'OUT':
        parked_cars.remove(car)
if parked_cars:
    for c in parked_cars:
        print(c)
else:
    print('Parking Lot is Empty')
