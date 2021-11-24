import ast


something = ast.literal_eval(input('Введите данные: '))
print(type(something))
if isinstance(something, dict):
    print('Тип данных:', type(something), '(словарь)', '\nИзменяемый (mutable)\nID объекта:', id(something))
elif isinstance(something, list):
    print('Тип данных:', type(something), '(список)', '\nИзменяемый (mutable)\nID объекта:', id(something))
elif isinstance(something, set):
    print('Тип данных:', type(something), '(множество)', '\nИзменяемый (mutable)\nID объекта:', id(something))
elif isinstance(something, bool):
    print('Тип данных:', type(something), '(логический)', '\nНеизменяемый (immutable)\nID объекта:', id(something))
elif isinstance(something, int):
    print('Тип данных:', type(something), '(целое число)', '\nНеизменяемый (immutable)\nID объекта:', id(something))
elif isinstance(something, float):
    print('Тип данных:', type(something), '(вещественное число)',
          '\nНеизменяемый (immutable)\nID объекта:', id(something))
elif isinstance(something, str):
    print('Тип данных:', type(something), '(строка)', '\nНеизменяемый (immutable)\nID объекта:', id(something))
elif isinstance(something, tuple):
    print('Тип данных:', type(something), '(кортеж)', '\nНеизменяемый (immutable)\nID объекта:', id(something))
