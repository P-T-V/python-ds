speakers_file = open('speakers.txt', 'r', encoding='utf-8')
sym_count = []
for i_line in speakers_file:
    print(i_line, end='')
    sym_count.append(str(len(i_line)))
print()
print(sym_count)
sym_count_str = '\n'.join(sym_count)
speakers_file.close()

couts_file = open('sym_count.txt', 'w')
couts_file.write(sym_count_str)
couts_file.write('\n')
couts_file.write(str(50))
couts_file.close()
