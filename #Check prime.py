#Check prime 
num = int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if num % i == 0:
            print("not prime")
            break
    else:
        print(num,"it's a prime number")
else: 
    print(num,"number must be greater than 1")