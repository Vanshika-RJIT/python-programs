a=2
print(id(a))
print(id(2))
a=a+1
print(id(3))
print(id(a))
b=2
print(id(2))
print(id(b))
def printhello():
    print("hello")
a=printhello()
print(a)
