class Car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.company="BMW"
c1=Car()
c2=Car()
c1.mil=12
Car.wheels=6
print(c1.mil,c1.company,Car.wheels)
print(c2.mil,c2.company,Car.wheels)
