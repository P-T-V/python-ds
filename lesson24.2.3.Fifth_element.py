BRUCE_WILLIS = 42
input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    print('leeloo =', leeloo)
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError:
    print("Unable to convert data to integer")
except IndexError:
    print("String index out of range")
except:
    print("Something goes wrong!")
