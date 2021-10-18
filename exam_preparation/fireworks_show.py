from collections import deque

effects = deque([int(x) for x in input().split(', ') if int(x) > 0])
power = deque([int(x) for x in input().split(', ') if int(x) > 0])

crossette_fireworks = 0
palm_fireworks = 0
willow_fireworks = 0

is_enough = False

while True:
    if (
        crossette_fireworks >= 3 and
        palm_fireworks >= 3 and
        willow_fireworks >= 3
    ):
        is_enough = True

    if not effects or not power:
        break

    result = effects[0] + power[-1]

    if result % 3 == 0 and result % 5 == 0: # crossette firework
        effects.popleft()
        power.pop()
        crossette_fireworks += 1

    elif result % 3 == 0: # palm firework
        effects.popleft()
        power.pop()
        palm_fireworks += 1

    elif result % 5 == 0:  # willow firework
        effects.popleft()
        power.pop()
        willow_fireworks += 1

    else:
        effects.append(effects.popleft() - 1)

if is_enough:
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    effects = list(map(lambda x: str(x), effects))
    print(f"Firework Effects left: {', '.join(effects)}")

if power:
    power = list(map(lambda x: str(x), power))
    print(f"Explosive Power left: {', '.join(power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")



