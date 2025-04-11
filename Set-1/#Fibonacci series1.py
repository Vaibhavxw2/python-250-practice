#Fibonacci series
n = int(input("Enter a number:"))
a = 0
b = 1
for i in range(0,n+1):
    print(a)
    sum = a + b
    a = b
    b = sum
    