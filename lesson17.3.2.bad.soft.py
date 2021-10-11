Fst_msg = input('Первое сообщение: ')
Snd_msg = input('Второе сообщение: ')
count1st = Fst_msg.count('!') + Fst_msg.count('?')
count2nd = Snd_msg.count('!') + Snd_msg.count('?')
Total_msg = []
if count1st > count2nd:
    # Total_msg.append(Fst_msg)
    # Total_msg.append(Snd_msg)
    print('\nТретье сообщение:', Fst_msg + Snd_msg)
elif count1st < count2nd:
    # Total_msg.append(Snd_msg)
    # Total_msg.append(Fst_msg)
    print('\nТретье сообщение:', Snd_msg + Fst_msg)
else:
    print('\nОй')
    