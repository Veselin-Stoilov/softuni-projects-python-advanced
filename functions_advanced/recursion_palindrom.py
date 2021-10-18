# def palindrome(word, index):
#     for i in range(len(word) // 2):
#         if word[i] != word[len(word) - 1 - i]:
#             return f"{word} is not a palindrome"
#     return f"{word} is a palindrome"


def palindrome(word, i):
    if i == len(word) // 2:
        return f"{word} is a palindrome"

    if word[i] != word[len(word) - 1 - i]:
        return f"{word} is not a palindrome"

    return palindrome(word, i + 1)


print(palindrome("abacaba", 0))
print(palindrome("peter", 0))

