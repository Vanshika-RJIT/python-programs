from array import *
a=array('i',[])
n=int(input("ENTER THE SIZE OF THE ARRAY"))
print("Enter the elements of array")
for i in range(n):
    x=int(input())
    a.append(x)
print(a)
val=int(input("Enter the element to search"))
'''k=1
for i in a:
    if(i==val):
        print(k)
        break
    k+=1'''
print(a.index(val))


