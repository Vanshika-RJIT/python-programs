dict={0:"1",1:"2",2:"3",3:{1:"G",2:"E",3:"E",4:"K",5:"S"}}
print(dict[0])
print(dict[3])
print(dict[3][3])
print(dict[1])
print(dict.popitem())
print(dict)
print(dict.pop(0))
print(dict)
del dict[1]
print(dict)
dict[3]={1:"GEEKS",2:"FOR",3:"GEEKS"}
print(dict)
del dict[3][1]
print(dict)
print(dict.clear())
print(dict)
