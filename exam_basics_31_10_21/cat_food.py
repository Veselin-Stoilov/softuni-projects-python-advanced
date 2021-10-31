food_price = 12.45
food_per_day = 0
group1 = 0
group2 = 0
group3 = 0

cats = int(input())

for cat in range(cats):
    food_per_cat = float(input())
    food_per_day += food_per_cat

    if 100 <= food_per_cat < 200:
        group1 += 1

    elif 200 <= food_per_cat < 300:
        group2 += 1

    elif 300 <= food_per_cat < 400:
        group3 += 1

price_per_day = (food_price / 1000) * food_per_day

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {price_per_day:.2f} lv.")
