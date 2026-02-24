n=list(map(int,input().split()))
m=int(input()) #upper point to break
p=int(input()) # divisble by this number
for i in n:
    if i>m:
        break
    elif i%p==0:
        print(i)
    
