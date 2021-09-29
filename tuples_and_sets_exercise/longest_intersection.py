first_set = set()
second_set = set()
longest_intersection = set()

for _ in range(int(input())):
    first_set = set()
    second_set = set()
    line = input().split('-')

    first_range_start = int(line[0].split(',')[0])
    first_range_end = int(line[0].split(',')[1])

    second_range_start = int(line[1].split(',')[0])
    second_range_end = int(line[1].split(',')[1])

    for num in range(first_range_start, first_range_end + 1):
        first_set.add(num)

    for num in range(second_range_start, second_range_end + 1):
        second_set.add(num)

    intersection = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

longest_intersection = list(map(lambda x: str(x), longest_intersection))

print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {len(longest_intersection)}')
