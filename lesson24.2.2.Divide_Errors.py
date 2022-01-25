def divide(number):
    return 10 / number


def sum_of_divided(left, right):
    div_sum = 0
    for i_num in range(left, right + 1):
        try:
            div_sum += divide(i_num)
            print(div_sum)
        except ZeroDivisionError:
            print("No-no-no! You can't divide by zero")
    return div_sum


total = 0
try:
    numbers_file = open('numbers1.txt', 'r')
    for i_line in numbers_file:
        nums_list = i_line.split()
        first_num = int(nums_list[0])
        second_num = int(nums_list[1])
        total += sum_of_divided(first_num, second_num)
    print('Total sum:', total)

except ZeroDivisionError:
    print("You can't divide by zero")

answer_file = open('answer.txt', 'w')
try:
    answer_file.write('The answer is: ')
    answer_file.write(str(total))
except TypeError:
    print('Argument must be string')
else:
    print("The program was executed without errors")
finally:
    answer_file.close()
    print(answer_file.closed)
