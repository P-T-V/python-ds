class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
        self.age = 0

    def print_info(self):
        print(f'Name: {self.name}\nSalary: {self.salary}\nAge: {self.age}\n')


emp_1 = Employee('Tom')
emp_2 = Employee('Bob', 20000)
emp_1.print_info()
emp_2.print_info()
