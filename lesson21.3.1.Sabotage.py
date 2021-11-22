text = input('Строка: ')
print('Ответ:', end=' ')
for i_index, i_symbol in enumerate(text):
    if i_symbol == '~':
        print(i_index, end=' ')
