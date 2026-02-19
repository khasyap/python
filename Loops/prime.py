n=int(input())
if n<0:
    print("Please enter a positive number")

elif n==0 or n==1:
    print("These are not a prime numbers")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime")