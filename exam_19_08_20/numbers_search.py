def numbers_searching(*args):
    values = list(args)
    missing_num = None
    duplicates = []
    for n in range(min(values), max(values)):
        if n not in values:
            missing_num = n

        else:
            if values.count(n) > 1:
                duplicates.append(n)

    result = list()
    result.append(missing_num)
    result.append(duplicates)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
