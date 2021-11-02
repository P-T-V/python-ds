words_list = []

for i_word in range(3):
    print('Введите', i_word + 1, 'слово:', end=' ')
    # word = input().lower()
    word = input().upper()
    words_list.append(word)

# text = input('Введите текст произведения: ').lower().split()
text = input('Введите текст произведения: ').upper().split()

print('\nПодсчёт слов в тексте:')
for id in range(3):
    print(words_list[id], ':', text.count(words_list[id]))
