msg = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

print('Список удвоенных символов:', [x * 2 for x in msg])
print('Склейка с дополнительным символом:', [x * 2 + symbol for x in msg])
