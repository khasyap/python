num = 20

for i in range(4, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num -= 2
    print()