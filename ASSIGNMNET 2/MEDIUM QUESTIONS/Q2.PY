#240280117049 NAYAK DEV

# Program to print first N Fibonacci numbers

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a)
    next_term = a + b
    a = b
    b = next_term
