nums_list = []

n = int(input('Кол-во собак: '))

for _ in range(n):
    num = int(input('Очки собаки: '))
    nums_list.append(num)

print(nums_list)

maximum = minimum = nums_list[0]

for i in nums_list:

    if maximum < i:
        maximum = i
    if minimum > i:
        minimum = i

for i in range(n):
    if nums_list[i] == maximum:
        nums_list[i] = minimum
    elif nums_list[i] == minimum:
        nums_list[i] = maximum

print('\n', nums_list)
