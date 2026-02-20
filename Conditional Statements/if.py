i = int(input())

if i <= 0:
    print("please enter a positive number")
elif i >= 90:
    print("1st")
elif i >= 80:
    print("2nd")
elif i >= 60:
    print("3rd")
elif i >= 35:
    print("pass")
else:
    print("Fail")
