#function definition
def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
print(add(10))
print("This is all about sum of natural numbers from 1 to 10")
def factorial(n):
    if n is 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print("This is all about factorial of number 5")
