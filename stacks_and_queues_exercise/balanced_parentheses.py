from collections import deque
parentheses = deque()
opening_parentheses_collection = deque()

opening_parentheses_types = ('{', '[', '(')
matches = ('{}', '[]', '()')
is_balanced = True
min_one_opening = False
min_one_closing = False

input_line = input()
for p in input_line:
    parentheses.append(p)

while parentheses:
    if parentheses[0] in opening_parentheses_types:
        min_one_opening = True
        opening_parentheses_collection.append(parentheses.popleft())
    else:
        if not opening_parentheses_collection:
            is_balanced = False
            break
        else:
            min_one_closing = True
            if opening_parentheses_collection.pop() + parentheses.popleft() not in matches:
                is_balanced = False
                break

if not (min_one_opening and min_one_closing):
    is_balanced = False
if is_balanced:
    print('YES')
else:
    print('NO')

