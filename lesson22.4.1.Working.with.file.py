def ask_user(question,
             compliant='Неверный ввод. Пожалуйста введите да или нет',
             retries=4):
    while True:
        answer = input(question).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Кол-во попыток закончилось.')
            break
        print(compliant)
        print('Осталось попыток:', retries)


ask_user('\nСохранить файл? ')
ask_user('\nЗаписать файл? ')
ask_user('\nУдалить файл? ', 'Точно удалить? ')
ask_user('\nПерезаписать файл? ', retries=2)
