class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show (self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i7'
            self.ram=16
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=Student("Khasyap",1)
s2=Student("Hari",2)
s1.show()
s2.show()