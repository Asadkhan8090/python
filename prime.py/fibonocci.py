n = int(input("Enter a number of items: "))
a = 0
b = 1
count = 0
while count < n:
    print(a, end='')
    c = a + b # next term is the sum of the last two terms
    a = b # update a to the last term
    count += 1 # increment the count