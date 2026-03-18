n=int(input())
s=set()
for i in range(n):
    
    k=i**2
    if k>10 and k%2!=0:
        s.add(k)
print(s)
