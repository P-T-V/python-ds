speakers_file = open('speakers.txt', 'r', encoding='utf-8')
second_stream = open('speakers.txt', 'r', encoding='utf-8')
data = speakers_file.read()
print(data)
print()
for i_line in second_stream:
    print(i_line, end='')
speakers_file.close()
second_stream.close()
