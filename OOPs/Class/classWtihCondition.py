class Result:
    def __init__(self, marks):
        self.marks = marks

    def check(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

r = Result(35)
r.check()