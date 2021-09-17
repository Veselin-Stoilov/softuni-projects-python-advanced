import sys
from io import StringIO
input_01 = """1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"""
input_02 = """(2 + 3) - (2 + 3)"""
#sys.stdin = StringIO(input_01)
#sys.stdin = StringIO(input_02)

line = input()
open_parentheses = []
close_parentheses = []
for index, el in enumerate(line):
    if el == '(':
        open_parentheses.append(index)
    if el == ')':
        start = open_parentheses.pop()
        end = index
        print(line[start: end + 1])
