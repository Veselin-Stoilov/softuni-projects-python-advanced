from collections import deque


def best_list_pureness(*args):
    values = deque(args[0])
    rotations = args[1]
    best_pureness = 0
    best_cycle = 0

    for cycle in range(rotations + 1):
        pureness = 0
        for n, i in enumerate(values):
            pureness += n * i
            if pureness > best_pureness:
                best_pureness = pureness
                best_cycle = cycle
        values.appendleft(values.pop())

    return f"Best pureness {best_pureness} after {best_cycle} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
