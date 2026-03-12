class Student:
    school="SVG"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is a Student class and it contains School module.")
s1=Student(22,24,23)
s2=Student(20,21,25)
print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
