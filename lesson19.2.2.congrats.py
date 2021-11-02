while True:
    grats_template = input('Введите шаблон поздравления, '
                           'в шаблоне нужно использовать конструкцию {name}: ')
    if '{name}' in grats_template:
        break
    print('Ошибка: отсутствует конструкция {name}.')

print('Введите список имён (заканчивается на end): ')
names_list = []
while True:
    name = input('Имя: ')
    if name != 'end':
        names_list.append(name)
    else:
        break

for i_name in names_list:
    print(grats_template.format(name=i_name))
