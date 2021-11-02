while True:
    grats_template = input('Введите шаблон поздравления, '
                           'в шаблоне нужно использовать конструкции {name} и {age}: ')
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print('Ошибка: отсутствует одна или две конструкции.')

names_list = input('Введите список людей через запятую: ').split(', ')
ages_str = input('Введите возраст людей через пробел: ')
ages = [int(i_number) for i_number in ages_str.split()]

for i_man in range(len(names_list)):
    print(grats_template.format(
        name=names_list[i_man],
        age=ages[i_man]
        )
    )
people = [
    ' '.join([names_list[i_man], str(ages[i_man])])
    for i_man in range(len(names_list))
]
people_str = ', '.join(people)
print('\nИменинники:', people_str)
