def caesar(text, move):
    new_ltrs = [all_letters[(all_letters.index(letter) + move) % len(all_letters)] if letter != ' ' else ' '
                for letter in text]
    caesar_text = ''.join(new_ltrs)

    return caesar_text


all_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
msg = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))

caesar_res = caesar(msg, shift)

print('Зашифрованное сообщение:', caesar_res)
