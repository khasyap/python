class Numbers:
    def __init__(self, arr):
        self.arr = arr

    def sum(self):
        total = 0
        for num in self.arr:
            total += num
        print("Sum =", total)

n = Numbers([1, 2, 3, 4])
n.sum()