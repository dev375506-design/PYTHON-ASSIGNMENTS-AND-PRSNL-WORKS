#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to calculate factorial of a number

num = int(input("Enter a number: "))

fact = 1

# factorial logic
for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "=", fact)
