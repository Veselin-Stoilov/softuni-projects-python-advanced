from collections import deque

males = deque(int(x) for x in reversed(input().split()) if int(x) > 0)
females = deque(int(x) for x in input().split() if int(x) > 0)

matches = 0

while True:
    if not males or not females:
        break

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()

    if males[0] % 25 == 0:
        males.popleft()
        males.popleft()

    if not males or not females:
        break

    if females[0] == males[0]:
        females.popleft()
        males.popleft()
        matches += 1
    else:
        females.popleft()
        males[0] -= 2
        if males[0] <= 0:
            males.remove(males[0])

print(f'Matches: {matches}')

if males:
    males = list(str(x) for x in males)
    print(f"Males left: {', '.join(males)}")
else:
    print("Males left: none")

if females:
    females = list(str(x) for x in females)
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")