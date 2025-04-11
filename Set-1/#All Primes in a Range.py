#All Primes in a Range 
n = int(input("Enter a number:"))
if n > 1:
    for i in range(2,n+1):
        if n % i == 0 :
            print(f"{i} is not prime")
        else:
            print(f"{i} is prine")
else:            
    print("Enter a number greater than 1")