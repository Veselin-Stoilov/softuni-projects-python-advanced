line = input().split()
line_reversed = []
for _ in range(len(line)):
    line_reversed.append(line.pop())
print(' '.join(line_reversed))