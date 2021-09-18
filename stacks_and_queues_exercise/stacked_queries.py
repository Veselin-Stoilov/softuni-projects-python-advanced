n = int(input())
stack = []
stack_reversed = []

for _ in range(n):
    command = input()
    if '1' in command:
        command = command.split()
        num = int(command[1])
        stack.append(num)
    else:
        if stack:
            if command == '2':
                stack.pop()
            elif command == '3':
                print(max(stack))
            elif command == '4':
                print(min(stack))
                
while stack:
    stack_reversed.append(stack.pop())
print(', '.join(map(str, stack_reversed)))
