print("----------Difference of max and min in array------------")
arr = [10, 5, 20, 8, 15]

difference = max(arr) - min(arr)

print("Difference:", difference)

print("----------Average in array------------")
arr = [10, 20, 30, 40]

average = sum(arr) / len(arr)

print("Average:", average)

print("----------sum of even in array------------")
arr = [1, 2, 3, 4, 5, 6]

even_sum = sum(num for num in arr if num % 2 == 0)

print("Sum of even numbers:", even_sum)


print("----------Count of duplicates in array------------")
arr = [1, 2, 2, 3, 4, 4, 4, 5]

duplicates = len(arr) - len(set(arr))

print("Number of duplicate elements:", duplicates)

print("----------Creating a Even array in array------------")
arr = [1, 2, 3, 4, 5, 6]

even = []

for num in arr:
    if num % 2 == 0:
        even.append(num)

print(even)



