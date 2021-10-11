pack_amt = int(input('Кол-во пакетов: '))
msg_pack = []
decode = []
lost_packs = 0

for i_pack_num in range(pack_amt):
    print('\nПакет номер', i_pack_num + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'бит:', end=' ')
        msg_pack.append(int(input()))
    if msg_pack.count(-1) <= 1:
        decode.extend(msg_pack)
    else:
        print('Много ошибок в пакете.')
        lost_packs += 1
    msg_pack = []

print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сообщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', lost_packs)