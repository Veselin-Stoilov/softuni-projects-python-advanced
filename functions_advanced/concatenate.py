def concatenate(*args):
    concat_str = ""
    for el in args:
        concat_str += el
    return concat_str


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))
