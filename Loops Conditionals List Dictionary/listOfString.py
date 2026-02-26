# Given a list of strings:
# words = ["Python", "java", "C", "javascript"]
# Filter words whose length is greater than 3
# Convert the filtered words to lowercase
# Find the total number of characters in the final list
words = ["Python", "java", "C", "javascript"]
s=set()
sum=0
for s1 in words:
    if len(s1)>3:
        s.add(s1)
print(s)
s2=str(s).lower()
print(s2)
for s1 in s:
    sum+=len(s1)
print(sum)
