x=int(input("Enter a number:"))
for i in range(1,x+1):
    if i*i==x:
        print("Given number is a perfect square number")
        break;
else:
    print("Given number is not a perfect square number")
import math
y=int(input("Enter a number:"))
x=math.sqrt(y)
if x-math.ceil(x)==0:
    print("Given number is a perfect square number")
else:
    print("Given number is not a perfect square number")

    
    
