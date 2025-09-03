num = int(input("Enter a nmber:"))
original = num
rev = 0

while num > 0:
    digital = num % 10
    rev = rev *10 + digital
    num = num // 10
    
if original == rev:
    print(f"{original} is a palindrome number.")
else:
    print(f"{original} is not a palindrome number.")
# This code checks if a number is a palindrome by reversing it and comparing it to the original number.