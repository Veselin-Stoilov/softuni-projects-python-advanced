first_set = set(input().split())
second_set = set(input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'Add' and command[1] == 'First':
        first_set = first_set.union((command[2:]))

    elif command[0] == 'Add' and command[1] == 'Second':
        second_set = second_set.union(command[2:])

    elif command[0] == 'Remove' and command[1] == 'First':
        first_set = first_set.difference(command[2:])

    elif command[0] == 'Remove' and command[1] == 'Second':
        second_set = second_set.difference(command[2:])
        
    elif command == 'Check Subset':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print('True')
        else:
            print('False')

first_set = list(map(lambda x: str(x), sorted(first_set)))
second_set = list(map(lambda x: str(x), sorted(second_set)))

print(', '.join(first_set))
print(', '.join(second_set))
