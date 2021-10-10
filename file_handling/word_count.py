searched_words_path = r'text_documents\words.txt'

full_text_path = r"text_documents\full_text.txt"

searched_content = 'quick is fault'

full_content = "-I was quick to judge him, but it wasn't his fault.\n" \
               "-Is this some kind of joke?! Is it?\n" \
               "-Quick, hide here…It is safer."

symbols = {'-', '_', '+', '!', '?', '.', ','}
words_count = {}

with open(searched_words_path, 'w') as searched_words_file:
    searched_words_file.write(searched_content)

sub_file = open(searched_words_path, 'r')
sub_file = [x.lower() for x in sub_file.read().split()]

with open(full_text_path, 'w') as full_text_file:
    full_text_file.write(full_content)

full_file = open(full_text_path, 'r')
full_file = list(full_file.read())

text_without_symbols = [x.lower() for x in full_file if x not in symbols]
text_without_symbols = ''.join(text_without_symbols).split()

for word in sub_file:
    count = text_without_symbols.count(word)
    words_count[word] = count

for w, c in sorted(words_count.items(), key=lambda kvp: kvp[1], reverse=True):
    print(f'{w}- {c}')
