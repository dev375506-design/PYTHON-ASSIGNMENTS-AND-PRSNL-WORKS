#240280117049 NAYAK DEV 

# Program to print all prime numbers from 1 to N
# Using square root optimization

import math   # used for sqrt()

N = int(input("Enter value of N: "))

print(f"Prime numbers from 1 to {N} are : ")

for num in range(2, N + 1):

    is_prime = True

    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
