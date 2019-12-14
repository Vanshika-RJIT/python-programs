from array import *
a=array('i',[1,34,45,56])
start=0
end=3
while(start<end):
    temp=a[start]
    a[start]=a[end]
    a[end]=temp
    start+=1
    end-=1
print("The array after the reversal:")
for i in range(4):
    print(a[i])
