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

List=[]
x=int(input("enter the number of elements in the list:"))
for i in range(x):
    num=int(input("enter a number:"))
    List.append(num)

Largest=max(List)
new_list=[]
for num in List:
    if num!=Largest:
        new_list.append(num)
print(f"The largest number is: {Largest}")


print(f"the second largest number is : {max(new_list)}")