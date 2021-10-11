n = int(input('Кол-во участников: '))
k = int(input('Кол-во человек в команде: '))
members = []
start_mem = 1

if n % k != 0:
    print(n, 'участников невозможно поделить на команды по', k, 'человек!')
else:
    for _ in range(n // k):
        members.append(list(range(start_mem, k + start_mem)))
        start_mem += k
    print('\nОбщий список команд:', members)
