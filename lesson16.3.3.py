user_words = []
count = [0, 0, 0]

for i in range(3):
    print('Введите', i + 1, 'слово:', end=' ')
    user_words.append(input())

text = input('\nСлово из текста: ')
while text != 'end':
    for id in range(3):
        if text == user_words[id]:
            count[id] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for id in range(3):
    print(user_words[id], ':', count[id])
