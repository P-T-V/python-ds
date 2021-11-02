while True:
    print('Введите 4 числа IP-адреса компьютера. Каждое число находится в диапазоне от 0 до 255 (включительно).')
    ip_list = []
    for i in range(4):
        flag = False
        print('Введите', i + 1, 'число:', end=' ')
        ip = int(input())
        if 0 <= ip <= 255:
            ip_list.append(ip)
        else:
            print('Ошибка: IP адрес вне диапазона')
            break
        flag = True
    if flag:
        break

ip_address = 'IP-адрес компьютера: {ip1}.{ip2}.{ip3}.{ip4}'.format(
    ip1=ip_list[0],
    ip2=ip_list[1],
    ip3=ip_list[2],
    ip4=ip_list[3]
)
print(ip_address)
