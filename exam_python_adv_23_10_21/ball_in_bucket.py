def world_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(input().split())
    return field


def step_outside(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def ball_in_bucket(r, c, world):
    if world[r][c] == 'B':
        world[r][c] = 0
        return True
    return False


def points_collection(r, c, world, points):
    steps = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
    }
    init_r, init_c = r, c
    for step in steps:
        r, c = init_r, init_c
        while True:
            next_r, next_c = steps[step](r, c)
            if step_outside(next_r, next_c, size):
                break
            r, c = next_r, next_c
            points += int(world[r][c])
    return points


size = 6
throws = 3
points = 0
field = world_generator(size)

for _ in range(throws):
    throw = input()
    row, col = (int(x) for x in throw[1: len(throw) - 1].split(', '))

    if step_outside(row, col, size):
        continue

    if ball_in_bucket(row, col, field):
        points = points_collection(row, col, field, points)


if points in range(100, 200):
    prize = 'Football'
elif points in range(200, 300):
    prize = 'Teddy Bear'
elif points >= 300:
    prize = 'Lego Construction Set'

if points < 100:
    points_needed = 100 - points
    print(f"Sorry! You need {points_needed} points more to win a prize.")

else:
    print(f"Good job! You scored {points} points, and you've won {prize}.")