user_words = input('Введите слова через пробел: ').split()
text = input('Введите текст произведения: ').split()
print(user_words)
print(text)
counter = []
for i_word in user_words:
    k = 0
    for i_text in text:
        if i_word == i_text:
            k += 1
    # counter.append(i_word + ' ' + str(k))
    counter.append(''.join([i_word, ': ', str(k)]))
print(counter)
print(', '.join(counter))
