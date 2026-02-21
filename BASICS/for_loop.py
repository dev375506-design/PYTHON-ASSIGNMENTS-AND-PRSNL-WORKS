# n=int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{n} (multiply) {i} = {n*i}")
# l = ["dev", "harry", "shanu", "swetabh", "soham"]

# for name in l:
#     if name.startswith("s"):   # check if name starts with 's'
#         print(f"Good morning {name}")


# n=int(input("enter a number: "))
# i=1
# while(i<11):
#     print(f"{n} (multiply) {i} = {n*i}")
#     i+=1
# n=int(input("enter the number: "))

# for i in range(2,n):
#     if(i%2)==0:
#         print("the number is not prime")
#         break
# else:
#         print("the number is prime")


# n=int(input("enter the number: "))
# i=0
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

n=int(input("enter the number: "))
product=1
for i in range(1,n+1):
    product=product*i
    
print(f"fact of {n} is ",product)