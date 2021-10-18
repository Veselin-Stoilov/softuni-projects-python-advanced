def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for i in range(len(args)):
        func_01 = args[i][0]
        params = args[i][1]
        calculation = func_01(*params)
        result.append(calculation)
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

      