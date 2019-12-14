
dic1={1:'vanshika',2:'sikarwar',3:'Gourav',4:'Baghel'}
dic2=dict([(1,'vanshika'),(2,'sikarwar')])
print(dic1[4])
#print(dic1[5])
print(dic1.get(5))
print(2 in dic1)
for i in dic2:
    print(dic2[i])
del dic2[1]
print(dic2)
'''del dic1
print(dic1)'''
dic3=dict({1:3,4:5})
dic3[4]='vanshika'
dic3[5]=5
print(dic3)
'''dic3.clear()
print(dic3)'''
print(dic3.pop(1))
print(dic3)
print(dic3.popitem())
print(dic3)


