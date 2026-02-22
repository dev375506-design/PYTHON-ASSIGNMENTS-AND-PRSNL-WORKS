#240280117049 NAYAK DEV

# Program to find sum of digits

num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print(f"Sum of digits = {sum}")
