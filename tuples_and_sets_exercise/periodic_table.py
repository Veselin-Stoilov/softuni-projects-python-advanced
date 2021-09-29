n = int(input())
elements_set = set()

for _ in range(n):
    current_elements = input().split()
    elements_set.union(current_elements)
    for el in current_elements:
        elements_set.add(el)
for el in elements_set:
    print(el)
