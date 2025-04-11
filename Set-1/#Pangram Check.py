#Pangram Check 
with open("Demo.txt", "r") as f:
    alp = "abcdefghijklmnopqrstuvwxyz"
    a = f.read().lower()
    for i in alp:
        if i in a:
            print("It's pangram")
            break
    else:
        print("It's not pangram")
        
    
