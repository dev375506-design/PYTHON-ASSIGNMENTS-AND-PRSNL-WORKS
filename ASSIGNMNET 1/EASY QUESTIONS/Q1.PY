#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to perform basic arithmetic operations


n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

addition = n1 + n2
difference = n1 - n2
product = n1 * n2


if n2 != 0:
    quotient = n1 / n2
else:
    quotient = "Undefined (cannot divide by zero)"


print(f"Addition: {n1} + {n2} = {addition}")
print(f"Subtraction: {n1} - {n2} = {difference}")   
print(f"Multiplication: {n1} * {n2} = {product}")
print(f"Division: {n1} / {n2} = {quotient}")
