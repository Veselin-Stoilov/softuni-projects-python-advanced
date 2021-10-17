nums = [int(x) for x in input().split()]
sum_positive = 0
sum_negative = 0

for n in nums:
    if n > 0:
        sum_positive += n
    else:
        sum_negative += n

print(sum_negative)
print(sum_positive)

if sum_positive > abs(sum_negative):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')