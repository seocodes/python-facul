phrase = input("Enter a phrase: ")

stripped_phrase = phrase.strip().replace(" ", "")

char_count = {}

for char in stripped_phrase:
    # o in verifica as chaves (keys) por padrão.
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"{char}: {count}")
