words = input('Введите строку: ')
search_sym = ':'
replace_sym = ';'
words_string = list(words)
# print(words_string)
count = 0
number = 0

print('Исправленная строка:', end=' ')
for i in words_string:
    if i == search_sym:
        words_string[number] = replace_sym
        count += 1
    print(words_string[number], end='')
    number += 1

print('\nКол-во замен:', count)
