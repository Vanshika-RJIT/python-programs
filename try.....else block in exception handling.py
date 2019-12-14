n=int(input("Enter a number:"))
try:
    c=3/n
except:
    print("ZeroDivisionError")
else:
    print("Exception is not raised"
          ,"c=",
          c)
