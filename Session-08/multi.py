word_to_find = "hello".upper()
user_word = "allol".upper()
result = [" "] * 5

for position in range(len(word_to_find)):
    if word_to_find[position] == user_word[position]:
        result[position] = word_to_find[position]

print(result)

for noitisop in range(len(user_word)):
    for position in range(len(word_to_find)):
        if word_to_find[position] == user_word[noitisop] and \
                not result[position] == user_word[noitisop]:
            result[position] = "-"

print(result)



