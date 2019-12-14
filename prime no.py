n=int(input("Enter the number which you want to check prime or not:"))
from math import sqrt 
for i in range(2,int(sqrt(n))+1):
    if(n%i==0):
        print("The given number is not a prime number")
        break
else:
    print("The given number is a prime number")
    
    
        
