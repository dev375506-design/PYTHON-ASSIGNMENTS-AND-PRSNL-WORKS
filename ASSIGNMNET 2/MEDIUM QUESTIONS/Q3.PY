#240280117049 NAYAK DEV

# Program to count digits in a number

num = int(input("Enter a number: "))

count = 0

while num != 0:
    num = num // 10
    count += 1

print("Total digits =", count)
