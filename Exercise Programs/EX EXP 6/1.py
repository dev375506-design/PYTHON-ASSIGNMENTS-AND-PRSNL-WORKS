def swap(a, b):
    return b, a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x, y = swap(x, y)

print("After swapping:")
print("x =", x, "y =", y)