phonebook_dict = {
    ('Petrov', 'Ivan'): 88006663636,
    ('Egorov', 'Ivan'): 88003333636,
    ('Ulyanov', 'Petr'): 88005553535,
    ('Sidorova', 'Lena'): 88007773737,
}

phonebook_dict[('Sidorova', 'Alena')] = 109090
for i_person in phonebook_dict:
    if 'Sidorova' in i_person:
        print(i_person[1], phonebook_dict[i_person])

print(phonebook_dict)
