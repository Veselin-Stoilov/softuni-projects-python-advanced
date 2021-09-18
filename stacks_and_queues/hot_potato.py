from collections import deque
import sys
from io import StringIO
input_01 = """Tracy Emily Daniel
2
"""
input_02 = """George Peter Michael William Thomas
10
"""
input_03 = """George Peter Michael William Thomas
1
"""
#sys.stdin = StringIO(input_01)
#sys.stdin = StringIO(input_02)
#sys.stdin = StringIO(input_03)
kids_names = deque(input().split())
n = int(input())
while len(kids_names) > 1:
    for i in range(n - 1):
        kids_names.append(kids_names.popleft())
    print(f'Removed {kids_names.popleft()}')

print(f'Last is {kids_names.popleft()}')
