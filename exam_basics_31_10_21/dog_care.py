available_food = int(input()) * 1000  # from kg to grams
consumed_food = 0
command = input()

while command != "Adopted":
    meal = int(command)
    consumed_food += meal
    command = input()

food_difference = abs(available_food - consumed_food)

if available_food >= consumed_food:
    print(f"Food is enough! Leftovers: {food_difference} grams.")

else:
    print(f"Food is not enough. You need {food_difference} grams more.")
