def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)

        c=a+b
        a=b
        b=c    
n=int(input())
fib(n)