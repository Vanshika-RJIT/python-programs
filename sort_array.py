from array import *
a=array('i',[1,2,34,5,4])
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if(a[j]>a[j+1]):
            tem=a[j]
            a[j]=a[j+1]
            a[j+1]=tem
print("The array after arranging in ascending order:"+str(a))
