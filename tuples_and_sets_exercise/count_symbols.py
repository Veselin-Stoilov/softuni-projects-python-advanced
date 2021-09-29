text = list(input())
unique_chars = set(text)
for char in sorted(unique_chars):
    print(f"{char}: {text.count(char)} time/s")
