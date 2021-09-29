set_first_len, set_second_len = [int(x) for x in input().split()]
set_first = set()
set_second = set()

for _ in range(set_first_len):
    set_first.add(int(input()))

for _ in range(set_second_len):
    set_second.add(int(input()))

unique_set = set_first.intersection(set_second)
for num in unique_set:
    print(num)
