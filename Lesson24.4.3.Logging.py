def palindrome(user_string, line):
    str_dict = dict()
    for i_symb in user_string:
        if i_symb.isdigit():
            raise BaseException('The digit in line No.{}!'.format(line))
        str_dict[i_symb] = str_dict.get(i_symb, 0) + 1
    odd_counter = 0
    for i_val in str_dict.values():
        if i_val % 2 != 0:
            odd_counter += 1
    if odd_counter <= 1:
        return True
    else:
        return False


palindrome_count = 0
line_count = 0
try:
    words_file = open('words.txt', 'r')
    for i_line in words_file:
        if i_line.endswith('\n'):
            cur_word = i_line[:-1]
        else:
            cur_word = i_line
        line_count += 1
        if len(cur_word) != 0:
            if palindrome(cur_word, line_count):
                palindrome_count += 1
except FileNotFoundError:
    print("File not found!")
except BaseException:
    print("The digit in line!!!")
    error_log = open('errors.log', 'w')
    error_log.write('ValueError. The digit(s) in line {}'.format(line_count))
    # error_log.write('\n')
    error_log.close()
    raise ValueError('The digit(s) in line {}'.format(line_count))
else:
    print("Program works normal")
finally:
    print("Total palindrome found:", palindrome_count)
    words_file.close()
    print(words_file.closed)
