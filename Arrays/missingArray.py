def missingArray(arr,low,high):
    arr_set=set(arr)
    missing_number=[]
    for num in range(low,high):
        if num not in arr:
            missing_number.append(num)
    return missing_number
arr=list(map(int,input().split()))
low=int(input())
high=int(input())
print(missingArray(arr,low,high))