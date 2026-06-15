# # n=int(input("enter a number:"))

# # a=0
# # b=1

# # for i in range(n):
# #     print(a)
# #     a,b=b,a+b

# n = int(input("Enter a number: "))
# # fact=1
# # # for i in range(1,n+1):
# # #     fact=fact*i
# # # print(f"The factorial of {n} is: {fact}")

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
    
# print(f"The factorial of {n} is: {factorial(n)}")


# n= int(input("Enter a number: "))
# def sum_digits(n):
#     sum = 0
#     while n!= 0:
#         digit=n%10
#         sum+=digit
#         n=n//10
#     return sum

# print(f"The sum of digits in {n} is: {sum_digits(n)}")


# num=int(input("enter a number to check if its palindrome or not:"))

# def is_palindrome(num):
#     original_num=num
#     reversed_num=0
#     while num>0:
#         digit=num%10
#         reversed_num=reversed_num*10+digit
#         num=num//10
#     return original_num==reversed_num

# if is_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")

# n=int(input("enter a number:"))
# t=0
# for i in range (0,n+1):
#     t=t+i
# print(f"The sum of first {n} natural numbers is: {t}")


# n=int(input("enter a number to get sum of its digits:"))
# def sum_digits(n):
#     sum = 0
#     while n!= 0:
#         digit=n%10
#         sum+=digit
#         n=n//10
#     return sum
# print(f"The sum of digits in {n} is: {sum_digits(n)}")


# name=input("enter your name:")
# print(len(name))

# List=[]
# x=int(input("enter the number of elements in the list:"))
# for i in range(x):
#     num=int(input("enter a number:"))
#     List.append(num)

# Largest=max(List)
# new_list=[]
# for num in List:
#     if num!=Largest:
#         new_list.append(num)
# print(f"The largest number is: {Largest}")


# print(f"the second largest number is : {max(new_list)}")

# numbers=[]
# n=int(input("enter number of elements in the list:"))
# for i in range(n):
#     num=int(input(f"enter the number {i+1}: "))
#     numbers.append(num)
# Largest=max(numbers)
# Minimum=min(numbers)
# Avg=sum(numbers)/len(numbers)
# print(f"The largest number is: {Largest}")
# print(f"The smallest number is: {Minimum}")
# print(f"The average of the numbers is: {Avg}")
# n = int(input("Enter number of elements: "))
# lst = []

# for i in range(n):
#     num = int(input("Enter number: "))
#     lst.append(num)

# largest = max(lst)
# lst.remove(largest)
# second = max(lst)

# print("Second largest number is:", second)
# import datetime
# def calculate_age(birth_year):
#     current_year = datetime.datetime.now().year
#     age = current_year - birth_year
#     return age
# birth_year = int(input("Enter your birth year: "))
# age = calculate_age(birth_year)
# print(f"You are {age} years old.")
# a=int(input("enter the first number: "))
# b=int(input("enter the second number: "))
# c=int(input("enter the third number: "))

# if a>b:
#     if a>c:
#         print(f"{a} is greatest")
#     else:
#         print(f"{c} is greatest")
# elif b>a:
#     if b>c:
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")
# else:
#     print("all numbers are equal")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# print(max(a, b, c), "is greatest")

# def swap(x,y):
#     return y,x
# x=int(input("enter the first number: "))
# y=int(input("enter the second number: "))
# print(f"Before swapping: x={x}, y={y}")
# x,y=swap(x,y)
# print(f"After swapping: x={x}, y={y}")
# def simple_interest(principal, rate, time):
#     interest = (principal * rate * time) / 100
#     return interest
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time in years: "))
# interest = simple_interest(principal, rate, time)
# print(f"The simple interest is: {interest}")
# def reverse_num(num):
#     reversed_num=0
#     while num>0:
#         digit=num%10
#         reversed_num=reversed_num*10+digit
#         num=num//10
#     return reversed_num
# n=int(input("enter a number to reverse: "))
# print(f"The reverse of {n} is: {reverse_num(n)}")

# def Leap_year(year):
#     if(year%4==0 and year%100!=0):
#         print(f"{year} is a leap year.")
#     elif(year%400==0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# year=int(input("enter a year to check if its leap year or not: "))
# Leap_year(year)

# def is_prime(num):
#     if num<=1:
#         print(f"{num} is not a prime number.")
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i==0:
#                 print(f"{num} is not a prime number.")
#                 break
#         else:
#             print(f"{num} is a prime number.")
# n=int(input("enter a number to check if its prime or not: "))
# is_prime(n)


# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Prime numbers are:")

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# n=int(input("enter to check: "))
# original_num=n

# def palindrome(n):
#     reversed_num=0
#     while n>0:
#         digit=n%10
#         reversed_num=reversed_num*10+digit
#         n=n//10
#     return reversed_num
# reversed_num=palindrome(n)
# if original_num==reversed_num:
#     print(f"{original_num} is a palindrome.")
# else:    print(f"{original_num} is not a palindrome.")

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(f"The factorial of {n} is: {factorial(n)}")

# n=int(input("eneter a no:"))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(f"The factorial of {n} is: {factorial(n)}")

# n=int(input("enter a number:"))

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b
# print(f"The first {n} numbers in the Fibonacci sequence are:")
# fibonacci(n)

# list=[]
# n=int(input("enter no of elements in the list : "))
# for i in  range(0,n):
#     num=int(input(f"enter {i+1} value to store in list: "))
#     list.append(num)
# print("the updted list is: ",list)
# max_list=max(list)
# min_list=min(list)
# sum_list=sum(list)
# avg_list=sum(list)/n

# print("the largest value in the list is:",max_list)
# print("the minimum value in the list is:",min_list)
# print("the sum value in the list is:",sum_list)
# print("the avg value in the list is:",avg_list)

# list=[]
# n=int(input("enter no of elements in the list : "))
# for i in  range(0,n):
#     num=int(input(f"enter {i+1} value to store in list: "))
#     list.append(num)
# print("the updted list is: ",list)
# even_no=[]
# odd_no=[]
# for num in list:
#     if num%2==0:
#         even_no.append(num)
#     else:
#         odd_no.append(num)
# greatest_of_even=max(even_no)
# greatest_of_odd=max(odd_no)

# print("greatest even no in the list is: ",greatest_of_even)
# print("greatest odd no in the list is: ",greatest_of_odd)


list=[]
n=int(input("enter no of elements in the list : "))
for i in  range(0,n):
    num=int(input(f"enter {i+1} value to store in list: "))
    list.append(num)
print("the updted list is: ",list)

x=int(input("eneter the element to count: "))
count=list.count(x)
print(f"The element {x} appears {count} times in the list.")