# a=int(input("enter the number a: "))
# b=int(input("enter the number b: "))
# c=int(input("enter the number c: "))
# def greatest():
#     if(a>b and a>c):
#         print("a is greatest")
#     elif(b>a and b>c):
#         print("b is greatest")
#     else:
#         print("c is greatest")
# greatest()



#celcius to fehrenheit

# degree = int(input("Enter the temp in degree: "))

# def convert():
#     fahrenheit = (9/5) * degree + 32
#     print("The temp in F is:", round(fahrenheit, 2))

# convert()


def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

n = int(input("Enter n: "))
print("Sum of first", n, "natural numbers is:", find_sum(n))
