
seq={1,2,3}
a=dict.fromkeys(seq)
print(a)
b=dict.fromkeys(seq,2)
print(b)
list=[2,3,4]
c=dict.fromkeys(seq,list)
print(c)
list.append(5)
print(c)