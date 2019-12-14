def reciprocal(n):
    try:
        c=1/n
    except ZeroDivisionError:
        print("1/n means 1/0","\n","divided by 0")
    except ValueError:
        print("Value is not determinable")
    except(TypeError,ValueError):
        print("Type is not determinable")
    else:
       print(c)

reciprocal(2)
reciprocal('hello')
reciprocal(0)
        
