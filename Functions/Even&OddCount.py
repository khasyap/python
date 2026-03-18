def evenOdd(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

list=[10, 12, 15, 13, 14, 120, 150]
even,odd=evenOdd(list)
print("Even :{} odd :{}".format(even,odd))