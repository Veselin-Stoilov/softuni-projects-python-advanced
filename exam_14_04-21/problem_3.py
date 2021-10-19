from collections import deque


def flights(*args):
    line = deque(args)
    destinations = {}
    while line:
        if line[0] == 'Finish':
            return destinations

        city = line.popleft()
        pax = line.popleft()

        if city not in destinations:
            destinations[city] = 0
        destinations[city] += pax
    return list(destinations)


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
