def even_odd(*args):
    line = list(args)
    result = []
    if line.pop() == 'even':
        result = [x for x in line if x % 2 == 0]
    else:
        result = [x for x in line if x % 2 != 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
