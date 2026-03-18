# You are given a list of numbers: nums = [10, 15, 20, 25, 30, 35, 40]
# Write a function that:Iterates over the list
# Creates a dictionary where:keys are the numbers
#values are:"Even" if the number is even "Odd" if the number is odd
# But skip numbers divisible by both 3 and 5

nums = [10, 15, 20, 25, 30, 35, 40]

def num(n):
    res={}
    for i in n:
        if i%2!=0:
            if i%3==0 and i%5==0:
                pass
            else:
                res[i]="Odd"
        elif i%2==0:
            res[i]="Even"
            
    return res
print(num(nums))