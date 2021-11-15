def palindrome(user_string):
    str_dict = dict()
    for i_symb in user_string:
        str_dict[i_symb] = str_dict.get(i_symb, 0) + 1
    counter = 0
    for i_val in str_dict.values():
        if i_val % 2 != 0:
            counter += 1
    if counter <= 1:
        return True
    else:
        return False


text = input('Введите строку: ')
if palindrome(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
