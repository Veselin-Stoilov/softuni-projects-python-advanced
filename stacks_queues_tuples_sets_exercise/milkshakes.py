from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milk and chocolates:

    if milkshakes == 5:
        break

    if chocolates[-1] <= 0:
        chocolates.pop()

    if milk[0] <= 0:
        milk.popleft()

    if milk and chocolates:
        if chocolates[-1] == milk[0]:
            chocolates.pop()
            milk.popleft()
            milkshakes += 1

        else:
            chocolates[-1] -= 5
            milk.append(milk.popleft())

chocolates = [str(x) for x in chocolates]
milk = [str(x) for x in milk]

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join(chocolates)}')
else:
    print('Chocolate: empty')

if milk:
    print(f'Milk: {", ".join(milk)}')

else:
    print(f'Milk: empty')

