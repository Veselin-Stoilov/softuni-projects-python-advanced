jobs = [int(x) for x in input().split(', ')]
index = int(input())

ordered_nums = sorted(jobs)
searched_num = jobs[index]

clock = 0
num_counter = 0

num_appearances = jobs[:index].count(searched_num)

for n in ordered_nums:
    if n == searched_num:
        if num_counter == num_appearances:

            clock += n
            break
        else:
            num_counter += 1

    clock += n

print(clock)
