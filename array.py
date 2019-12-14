from array import *
a=array('i',[3,4,-5,67,1])
print(a.typecode)
#a.byteswap()
#print(a)
print(a.buffer_info())
new_a=array(a.typecode,(a for a in a))
i=0
while i<len(new_a):
    print(new_a[i])
    i+=1
