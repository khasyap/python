class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

s = Student("Surya", 90)
t = Teacher("Ram", "Math")

print(s.name, s.marks)
print(t.name, t.subject)