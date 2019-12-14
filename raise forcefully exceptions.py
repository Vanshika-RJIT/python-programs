def input(n):
    try:
        if(n<=0):
            raise TypeError
    except TypeError:
        print("Not a positive integer")
    else:
        print("A positive integer")
input(4)
input(-3)
