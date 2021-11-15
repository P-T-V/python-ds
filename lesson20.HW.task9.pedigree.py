# humans = int(input('Введите количество человек: '))
# humans_dict = dict()
pedigree_dict = dict()

# for i_pair in range(1, humans):
#     print(i_pair, 'пара:', end=' ')
#     pair = input().split()
#     humans_dict[pair[0]] = pair[1]

# # Пары родитель-ребёнок для ускорения ввода информации:
humans_dict = {
    'Alexei': 'Peter_I',
    'Anna': 'Peter_I',
    'Elizabeth': 'Peter_I',
    'Peter_II': 'Alexei',
    'Peter_III': 'Anna',
    'Paul_I': 'Peter_III',
    'Alexander_I': 'Paul_I',
    'Nicholaus_I': 'Paul_I'
}

# print('Пары родитель-ребёнок:')
# for i_pair in humans_dict:
#     print(i_pair, humans_dict[i_pair])

all_set = set(humans_dict.keys()) | set(humans_dict.values())
head_set = all_set - set(humans_dict.keys())

pedigree_dict[list(head_set)[0]] = 0
print(pedigree_dict)
i = 1

curr_head_set = head_set
while len(curr_head_set) > 0:
    for i_pair in humans_dict:
        if humans_dict.get(i_pair) in curr_head_set:
            pedigree_dict[i_pair] = i
    i += 1
    head_set = head_set | curr_head_set
    curr_head_set = set(pedigree_dict.keys()) - head_set

print('\n“Высота” каждого члена семьи:')
for i_pair in sorted(pedigree_dict):
    print(i_pair, pedigree_dict[i_pair])
