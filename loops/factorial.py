n=int(input("enter a number to get factorial: "))

product=1
for i in range(1,n+1):
    product=product*i
    factorial=product

# factorial=1
# i=1
# while(i<=n):
#     factorial=factorial*i
#     i+=1
print(f"factorial of {n} is {factorial}.")