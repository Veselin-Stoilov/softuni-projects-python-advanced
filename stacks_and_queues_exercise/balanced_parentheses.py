from collections import deque
input_queue = deque()
opening_brackets = deque()
matches = ('{}', '[]', '()')
opening_options = ('{', '[', '(')
is_balanced = True
line = input()

for i in line:
    input_queue.append(i)

while input_queue:
    if input_queue[0] in opening_options:
        opening_brackets.append(input_queue.popleft())
    else:
        if opening_brackets.pop() + input_queue.popleft() not in matches:
            is_balanced = False
            break
        else:
            continue

if not is_balanced or opening_brackets is True:
    print('NO')
else:
    print('YES')

