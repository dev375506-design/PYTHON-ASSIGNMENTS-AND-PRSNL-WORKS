#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to print all prime numbers from 1 to N
# Using square root optimization

import math   # used for sqrt()

N = int(input("Enter value of N: "))

print("Prime numbers between 1 and", N, "are:\n")

# Loop from 2 to N
for num in range(2, N + 1):

    is_prime = True

    # check divisibility only till square root of number
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
