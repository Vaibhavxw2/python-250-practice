#Anagram Check
a = input("Enter a numkber:")
b = input("Enter a number:")
str1 = a.replace(" ", "").lower()
str2= b.replace(" ","").lower()
if sorted(str1)== sorted(str2) :
    print("it's anagram")
else:
    print("it's not anargram")
    