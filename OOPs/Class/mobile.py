class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 20000)
m2 = Mobile("Apple", 80000)

print(m1.brand, m1.price)
print(m2.brand, m2.price)