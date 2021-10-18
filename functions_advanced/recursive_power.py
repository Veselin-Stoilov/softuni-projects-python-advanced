def recursive_power(base, n):
    if n == 0:
        return 1
    if n >= 1:
        result = base * recursive_power(base, n - 1)
        return result


print(recursive_power(2, 5))
print(recursive_power(10, 100))


