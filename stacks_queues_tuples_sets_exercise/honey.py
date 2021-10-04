from collections import deque


def addition(bee, nectar):
    return abs(bee + nectar)


def subtraction(bee, nectar):
    return abs(bee - nectar)


def multiplication(bee, nectar):
    return abs(bee * nectar)


def division(bee, nectar):
    if nectar != 0:
        return abs(bee // nectar)


honey = 0

bees = deque([int(x) for x in input().split()])
nectar_values = deque([int(x) for x in input().split()])
operators = deque(input().split())


operators_dict = {
    '+': addition(bees.popleft(), nectar_values.pop()),
    '-': subtraction(bees.popleft(), nectar_values.pop()),
    '*': multiplication(bees.popleft(), nectar_values.pop()),
    '/': division(bees.popleft(), nectar_values.pop()),
}


while bees and nectar_values and operators:
    if bees[0] > nectar_values[-1]:
        nectar_values.pop()
    elif bees[0] <= nectar_values[-1]:
        honey += operators_dict[operators.popleft()]

print(honey)

print(bees)
print(nectar_values)

