from array import *
a=array('i',[1,23,45,67])
pos=int(input("Enter the element position which you want to display:"))
for i in range(pos-1,3):
    a[i]=a[i+1]
for i in range(3):
    print(a[i])
    
    
