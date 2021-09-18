from collections import deque
from io import StringIO
import sys
input_01 = """348
20 54 30 16 7 9
"""
input_02 ="""499
57 45 62 70 33 90 88 76 100 50
"""
#sys.stdin = StringIO(input_01)
#sys.stdin = StringIO(input_02)
food_quantity = int(input())
orders_queue = deque(map(int, input().split()))
print(max(orders_queue))
for _ in range(len(orders_queue)):
    if orders_queue[0] <= food_quantity:
        food_quantity -= orders_queue.popleft()
    else:
        break
if orders_queue:
    print('Orders left:', end=' ')
    while orders_queue:
        print(orders_queue.popleft(), end=' ')
else:
    print('Orders complete')