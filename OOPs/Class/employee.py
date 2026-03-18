class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

name = input("Enter name: ")
salary = int(input("Enter salary: "))

e1 = Employee(name, salary)

print(e1.name, e1.salary)