import sys
from time import time
from io import StringIO
line_01 = """abcdef"""
line_02 = """123456789"""

#sys.stdin = StringIO(line_01)
#sys.stdin = StringIO(line_02)
line_ss = []
result = ''
line = input()
for el in line:
    line_ss.append(el)

while line_ss:
    result += line_ss.pop()
print(result)

