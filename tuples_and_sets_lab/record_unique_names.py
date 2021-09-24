n = int(input())
names_set = set()
for _ in range(n):
    names_set.add(input())
for name in names_set:
    print(name)