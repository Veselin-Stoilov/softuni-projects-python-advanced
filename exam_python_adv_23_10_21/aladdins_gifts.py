from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

gifts = {}
gifts_created = False

while True:
    if not materials or not magic:
        break

    result = materials[-1] + magic[0]

    if result < 100:
        if result % 2 == 0:
            materials[-1] *= 2
            magic[0] *= 3
            result = materials[-1] + magic[0]

        elif result % 2 != 0:
            result *= 2

    if result >= 500:
        result /= 2

    if 100 <= result < 200:
        gift = 'Gemstone'
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1

    elif 200 <= result < 300:
        gift = 'Porcelain Sculpture'
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1

    elif 300 <= result < 400:
        gift = 'Gold'
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1

    elif 400 <= result < 500:
        gift = 'Diamond Jewellery'
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1

    materials.pop()
    magic.popleft()

if 'Gemstone' in gifts and 'Porcelain Sculpture' in gifts:
    gifts_created = True

elif 'Gold' in gifts and 'Diamond Jewellery' in gifts:
    gifts_created = True

if gifts_created:
    print('The wedding presents are made!')

else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    materials = [str(x) for x in materials]
    print(f"Materials left: {', '.join(materials)}")

if magic:
    magic = [str(x) for x in magic]
    print(f"Magic left: {', '.join(magic)}")

for k, v in sorted(gifts.items()):
    print(f'{k}: {v}')





