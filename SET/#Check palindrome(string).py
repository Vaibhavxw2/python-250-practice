#Check palindrome(string)
str = input("Enter a string:")
str1 = str[::-1]
if str1 == str:
    print("It's palindrome")
else:
    print("It's not a palindrome")