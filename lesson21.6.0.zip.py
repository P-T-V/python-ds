names = ['Tom', 'Bob', 'Albert']
ages = [20, 45, 70, 100]

people = zip(names, ages)
print(people)
for i_person in people:
    print(i_person)

people2 = dict(zip(names, ages))
print('\n', people2)
for i_person, i_age in people2.items():
    print(i_person, i_age)

people3 = {
    i_name: i_age + 10
    for i_name, i_age in zip(names, ages)
}
print('\n', people3)
