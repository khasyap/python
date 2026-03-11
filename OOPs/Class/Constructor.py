class Constructor:
    def __init__(self):
        self.name="khasyap"
        self.age=20
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
person1=Constructor()
person1.age=30
person2=Constructor()

if person1.compare(person2):
    print("They are same")
else:
    print("They are different")
print(person1.name,person1.age)
print(person2.name,person2.age)
