delivery = input()
rack_capacity = int(input())
clothes_stack = list(map(int, delivery.split()))
weight_counter = 0
racks_counter = 1
for _ in range(len(clothes_stack)):
    if weight_counter + clothes_stack[-1] > rack_capacity:
        racks_counter += 1
        weight_counter = clothes_stack.pop()
    else:
        weight_counter += clothes_stack.pop()
print(racks_counter)

