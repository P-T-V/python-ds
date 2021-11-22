import random


def new_dict():
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    list_rand = [random.choice(alphabet) for _ in range(10)]
    dict_rand = dict()
    for i_index, i_symb in enumerate(list_rand):
        dict_rand[i_index] = i_symb
    return list_rand, dict_rand


list1, dict1 = new_dict()
list2, dict2 = new_dict()

print('Первый список:', list1)
print('Второй список:', list2)
print('\nПервый словарь:', dict1)
print('Второй словарь:', dict2)
