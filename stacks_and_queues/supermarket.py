from io import StringIO
import sys
from collections import deque
input_01 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End
"""
input_02 = """Anna
Emma
Alexander
End
"""
#sys.stdin = StringIO(input_01)
#sys.stdin = StringIO(input_02)
line = input()
queue = deque()
while line != 'End':
    if line == 'Paid':
        while queue:
            print(queue.popleft())
    if line != 'Paid':
        queue.append(line)
    line = input()
print(f'{len(queue)} people remaining.')
