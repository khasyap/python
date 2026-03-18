from functools import reduce
lis=[10,12,13,1,2,5,6,3,8]
even=list(filter(lambda n:n%2==0,lis))

print(even)
add=list(map(lambda n:n+2,even))
print(add)
mul=list(map(lambda n:n*2,even))
print(mul)
sum=reduce(lambda a,b:a+b,mul)
print(sum)