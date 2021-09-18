from collections import deque
import sys
from io import StringIO
input_01 = """2
Peter
Amy
Start
2
refill 1
1
End
"""
input_02 = """10
Peter
George
Amy
Alice
Start
2
3
3
3
End
"""
#sys.stdin = StringIO(input_01)
#sys.stdin = StringIO(input_02)
water_quantity = int(input())
name = input()
queue = deque()
while name != 'Start':
    queue.append(name)
    name = input()

command = input()
while command != 'End':
    command = command.split()
    if len(command) == 1:
        water_used = int(command[0])
        if water_used <= water_quantity:
            water_quantity -= water_used
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')
    elif len(command) == 2:
        water_added = int(command[1])
        water_quantity += water_added
    command = input()
print(f'{water_quantity} liters left')



