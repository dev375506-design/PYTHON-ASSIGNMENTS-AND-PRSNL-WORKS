#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to perform basic arithmetic operations

# Taking two integers from user
n1 = int(input("Enter first integer: "))
n2 = int(input("Enter second integer: "))

# Calculations
sum_result = n1 + n2
difference = n1 - n2
product = n1 * n2

# Checking division by zero
if n2 != 0:
    quotient = n1 / n2
else:
    quotient = "Undefined (cannot divide by zero)"

# Displaying results
print("\n--- Results ---")
print("Sum =", sum_result)
print("Difference =", difference)
print("Product =", product)
print("Quotient =", quotient)
