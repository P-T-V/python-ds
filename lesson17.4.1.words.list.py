user_words = [['', 0], ['', 0], ['', 0]]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    word = input()
    user_words[i][0] = word

text = input('\nСлово из текста: ')
while text != 'end':
    for id in range(3):
        if text == user_words[id][0]:
            user_words[id][1] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for id in range(3):
    print(user_words[id][0], ':', user_words[id][1])
    