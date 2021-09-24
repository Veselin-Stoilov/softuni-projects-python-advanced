nums = [float(x) for x in input().split()]
num_set = set()
counter = 0
for num in nums:
    if num in num_set:
        continue
    else:
        num_set.add(num)
        print(f"{num} - {nums.count(num)} times")



