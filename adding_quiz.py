def add(a, b):
    return a + b
    # print(a + b)
    # if you don't have a `return`
    # your function automatically
    # returns `None`

# Write a function that can be called like so:
add(1, 1)
# I expect the result to be 2

num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))
print(add(add(num1, num2), num3))
# And the result be 3
# Hint: the function should not print()
 
