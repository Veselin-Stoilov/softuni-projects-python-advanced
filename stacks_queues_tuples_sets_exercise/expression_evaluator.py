from collections import deque


def multiplication(int_list):
    result = int_list.popleft()
    while int_list:
        result *= int_list.popleft()
    return result


def addition(int_list):
    result = int_list.popleft()
    while int_list:
        result += int_list.popleft()
    return result


def subtraction(int_list):
    result = int_list.popleft()
    while int_list:
        result -= int_list.popleft()
    return result


def division(int_list):
    result = int_list.popleft()
    while int_list:
        result //= int_list.popleft()
    return result


string = deque(input().split())
operands = deque()

while len(string) > 0:
    if string[0].isdigit():
        operands.append(int(string.popleft()))
    elif len(string[0]) > 1 and string[0].startswith('-'):
        operands.append(int(string.popleft()))

    elif string[0] == '*':
        string.popleft()
        operands.appendleft(multiplication(operands))

    elif string[0] == '+':
        string.popleft()
        operands.appendleft(addition(operands))

    elif string[0] == '-':
        string.popleft()
        operands.appendleft(subtraction(operands))

    elif string[0] == '/':
        string.popleft()
        operands.appendleft(division(operands))

print(operands[0])