user_words = input('Введите строку: ').split()
# user_letters = user_text.split()
big_letters = 0
small_letters = 0

for word in user_words:
    for letter in word:
        if letter.isupper():
            big_letters += 1
        else:
            small_letters += 1

if big_letters >= small_letters:
    new_text = ' '.join(user_words).upper()
else:
    new_text = ' '.join(user_words).lower()
print('Результат:', new_text)
