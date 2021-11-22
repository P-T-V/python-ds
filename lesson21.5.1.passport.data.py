data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

passport_series = int(input('Введите серию паспорта: '))
passport_number = int(input('Введите номер паспорта: '))

for i_pass in data:
    if (passport_series, passport_number) == i_pass:
        print(i_pass, data[i_pass])
