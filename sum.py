# # def fact(n):
# #     fact=1
# #     for i in range (1,n+1):
# #         fact=fact*i
# #     return fact
# # n=int(input("enter a number:"))
# # print(f"The factorial of {n} is: {fact(n)}")


# # Function to calculate factorial
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# # Input from user
# num = int(input("Enter a number: "))

# # Function call
# result = factorial(num)

# # Display result
# print("Factorial is:", result)


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b   # return swapped values

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)  # capture returned values

print(f"After swapping: a={a}, b={b}")
