dic1={1:"V",2:"A",3:"N",4:"S",5:"H"}
dic=dic1.copy();
dic1.clear();
print("The given dictionary:"+str(dic))
print("The given dictionary after copying:"+str(dic1))
print(dic.get(2))
res1=dic.pop(1)
print(res1)
print(dic)
res2=dic.popitem()
print(res2)
print(dic)

