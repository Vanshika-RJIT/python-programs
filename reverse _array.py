from array import *
a=array('i',[1,2,3,56])
for i in range(3):
    for j in range(i+1,4):
        a[j]=a[i]
print(a)
    
