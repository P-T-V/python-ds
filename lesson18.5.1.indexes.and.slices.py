word = 'Привет'

first_part = word[:(len(word)) // 2]
print(first_part[::-1])

snd_part = word[(len(word)) // 2:]
print(snd_part[::-1])

print(first_part[::-1] + snd_part[::-1])
