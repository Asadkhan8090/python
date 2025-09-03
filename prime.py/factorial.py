# for loop
n = int(input("Enter a number:"))
factorial = 1
for i in range(1, n+1):
    factorial *= i # multipaly each number to get the factorial
print(f"The factorial of {n} is: {factorial}")    






num = int(input("Enter the number:"))
factorial = 1
if num < 0:
    print("factorial is not defined for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
        print(f"the factorial of {num} is: {factorial}")        