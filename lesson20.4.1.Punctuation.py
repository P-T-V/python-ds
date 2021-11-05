# text = input('Введите строку: ')
text_set = set(input('Введите строку: '))
symbols = set('.,;:!?')
# text_symbols = text_set.intersection(symbols)
# text_symbols = text_set & symbols
# print(text_symbols)
# print(symbols)
print('Количество знаков пунктуации:', len(text_set & symbols))
