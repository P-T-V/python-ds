words = input('Введите строку: ')
words_string = list(words)
id = int(input('Номер символа: '))

counter = 0
sym_all = 0
for i in words_string:
    sym_all += 1

if id != 1:
    print('Символ слева:', words_string[id - 2])
    if words_string[id - 2] == words_string[id - 1]:
        counter += 1

if id != sym_all:
    print('Символ справа:', words_string[id])
    if words_string[id] == words_string[id - 1]:
        counter += 1

if counter == 2:
    print('Есть ровно два таких же символа')
elif counter == 1:
    print('Есть ровно один такой же символ')
else:
    print('Таких же символов нет')
