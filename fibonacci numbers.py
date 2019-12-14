n=int(input("Enter the number upto you want fibonacci series:"))
f=0
b=1
print(f,end=" ")
print(b,end=" ")
for i in range(1,n-2+1):
      c=f+b
      print(c,end=" ")
      f=b
      b=c


