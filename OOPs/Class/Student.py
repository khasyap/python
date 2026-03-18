class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = [
    Student("Surya", 85),
    Student("Ram", 92),
    Student("Krishna", 88)
]

top = max(students, key=lambda s: s.marks)

print("Top student:", top.name, top.marks)