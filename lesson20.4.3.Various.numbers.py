# text = input('Введите строку: ')
text = set('ab1n32kz2')
print(text)
# '0'<=x<='9'
digits = set([str(x) for x in range(10)])
# print(digits)
# uniqe_digits = text & digits
# print('Различные цифры строки:', ''.join(uniqe_digits))
print('Различные цифры строки:', ''.join(text & digits))
