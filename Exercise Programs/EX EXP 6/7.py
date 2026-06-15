def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    return sum == num

n = int(input("Enter number: "))

if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not Armstrong number")