# Program to check whether a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a prime number")
else:
    is_prime = True

    # check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num}is a Prime Number")
    else:
        print(f"{num}is NOT a Prime Number")
