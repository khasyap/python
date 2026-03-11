class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("Configure is ", self.cpu,self.ram)
comp1=computer('i5',16)
comp2=computer('Ryzen',8)
computer.config(comp1)
computer.config(comp2)
