n = int(input())
r = n + 1
even_nums = set()
odd_nums = set()
for row in range(1, r):
    ch_sum = 0
    name = input()
    for ch in name:
        ch_sum += ord(ch)
    ch_sum //= row
    if ch_sum % 2 == 0:
        even_nums.add(ch_sum)
    else:
        odd_nums.add(ch_sum)

even_sum = sum(even_nums)
odd_sum = sum(odd_nums)

if even_sum == odd_sum:
    result = odd_nums.union(even_nums)

elif odd_sum > even_sum:
    result = odd_nums.difference(even_nums)

elif odd_sum < even_sum:
    result = odd_nums.symmetric_difference(even_nums)

result = list(map(lambda x: str(x), result))
print(', '.join(result))