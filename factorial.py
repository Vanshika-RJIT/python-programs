num=int(input("Enter the number to find factorial:"))
f=1
for i in range(num,0,-1):
    f=f*i
print("The factorial of given number:"+str(f))
