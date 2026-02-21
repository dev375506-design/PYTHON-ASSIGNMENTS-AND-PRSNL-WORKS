#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to find the largest among three numbers

# Taking three numbers from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Checking largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Display result
print("The largest number is:", largest)
