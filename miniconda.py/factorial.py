# using recursion
def factorial(n):
    if n == 0 or n == 1: # a base case
        return 1
    else:
        return n * factorial(n - 1) # recursive  call
    num = int(input("Enter a number:"))
    if num < 0:
        print("factorial is not defined for negative numbers.")
    elif num == 0:
        print("the factorial of 0 is: 1")
    else:
        print(f"the factorial of {num} is: {factorial(num)}") # call the function
            