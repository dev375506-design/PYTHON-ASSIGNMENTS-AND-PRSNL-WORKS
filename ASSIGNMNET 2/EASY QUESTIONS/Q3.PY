#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV
# Program to calculate factorial of a number


# 1st is with loops and 2nd is with recursion


n= int(input("Enter a number: "))

fact = 1


for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n} is {fact}")

# Factorial with recursion

def factorial(n):
    if n == 0 or n == 1:   
        return 1
    else:
        return n * factorial(n - 1)  



if n < 0:
    print("Factorial not defined for negative numbers")
else:
    print(f"Factorial of {n} is {factorial(n)}")
    

   