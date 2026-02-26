# Given a list:
# data = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
# Using one line of code:
# Create a set of squares of only odd numbers
# The square must be greater than 10
# Expected output:
# {25, 49}
data=[1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
s=set()
for i in data:
    
    k=i**2
    if k>10 and k%2!=0:
        s.add(k)
print(s)
