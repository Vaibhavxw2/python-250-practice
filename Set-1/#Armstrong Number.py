#Armstrong Number
num = input("Enter a number:")
a = 0
for i in num:
    ab = int(i)
    a += ab**len(num)
if a == int(num):
    print("It's Armstrong")
else:
    print("It's not Armstrong")