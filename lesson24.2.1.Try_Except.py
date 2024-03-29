nums_sum = 0
nums_count = 0
try:
    numbers_file = open('numbers.txt', 'r')
    for i_line in numbers_file:
        nums_count += 1
        nums_sum += int(i_line)
    numbers_file.close()
    print('Arithmetic mean:', nums_sum / nums_count)
except FileNotFoundError:
    print('File not found')
except ValueError:
    print("Unable to convert data to integer")
