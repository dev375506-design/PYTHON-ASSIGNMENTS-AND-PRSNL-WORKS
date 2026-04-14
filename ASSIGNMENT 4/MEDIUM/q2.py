#NAYAK DEV_240280117049

n = int(input("Enter number of elements: "))
my_dict = {}

for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    my_dict[key] = value

total = sum(my_dict.values())
print("Sum:", total)