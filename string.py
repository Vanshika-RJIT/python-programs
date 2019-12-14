string=input("Enter the string:")
a=0
big=0
for i in range(0,len(string)):
    if(a<string.count(string[i])):
        big=string.count(string[i])
    else:
        big=a
print("The maximum occurencing:"+str(string[i]))
