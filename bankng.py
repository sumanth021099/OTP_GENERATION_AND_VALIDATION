import random
n=0
while(n<3):
    a=random.randrange(99999,999999)
    
    print(a)
    b=int(input("enter otp:"))

    if a==b:
        print("transaction approved")
        break
    else:    
    
        
        n=n+1
if n==3:
    print("transaction failed")
