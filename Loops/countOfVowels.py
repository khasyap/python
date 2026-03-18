text = "hello world"

vowels = "aeiou"

count = sum(1 for char in text if char in vowels)

print("Vowel count:", count)