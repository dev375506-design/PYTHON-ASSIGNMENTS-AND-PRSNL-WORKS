#240280117049 NAYAK DEV

# Program to find sum of first N natural numbers

n = int(input("Enter value of n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(f"Sum of first {n} natural numbers is {sum}")
