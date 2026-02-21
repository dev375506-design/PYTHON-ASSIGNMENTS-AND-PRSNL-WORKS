n=int(input("enter a number to be checked for prime: "))

for i in range(2,n):
    if(n%2==0):
        print(f"{n} is not a prime number.")
        break
    else:
        print(f"{n} is a prime number.")
        break