n =input()
if isinstance(n, int):
    print("This input is of type integer")
elif isinstance(n, float):
    print("This input is of type float")
elif isinstance(n, str):
    print("This input is of type string")
else:
    print("This is something else")
