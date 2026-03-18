#method 1:
a,b=map(int,input().split())
a,b=b,a
print(a,b)

#method 2:
a,b=map(int,input().split())
temp=a
a=b
b=temp
print(a,b)

#method 3:
a,b=map(int,input().split())
a=a+b
b=a-b
a=a-b
print(a,b)
