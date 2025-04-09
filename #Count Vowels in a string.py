#Count Vowels in a string
str = input("Enter a string:")
count = 0
vowels = "aeiouAEIOU"
for char in str:
    if char in vowels:
        count += 1
print(count)
