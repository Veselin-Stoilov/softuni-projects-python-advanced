locations = int(input())

for location in range(locations):
    gold_total = 0
    day_target = float(input())
    days_per_location = int(input())

    for day in range(days_per_location):

        gold_per_day = float(input())
        gold_total += gold_per_day

    average_per_day = gold_total / days_per_location
    if average_per_day >= day_target:
        print(f"Good job! Average gold per day: {average_per_day:.2f}.")
    else:
        needed_per_day = day_target - average_per_day
        print(f"You need {needed_per_day:.2f} gold.")