from functools import reduce

n=[13,2,5,6,8,9,3,14,55,62,31,35]
odd=list(filter(lambda o:o%2!=0,n))
print(odd)
add=list(map(lambda a:a+2,odd))
print(add)
mul=list(map(lambda b:b*2,add))
print(mul)
sum=reduce(lambda a,b:a+b,mul)
print(sum)