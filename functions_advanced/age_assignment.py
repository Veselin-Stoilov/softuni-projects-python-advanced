def age_assignment(*args, **kwargs):
    pax_info = {}
    for name in args:
        pax_info[name] = kwargs[name[0]]
    return pax_info


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
