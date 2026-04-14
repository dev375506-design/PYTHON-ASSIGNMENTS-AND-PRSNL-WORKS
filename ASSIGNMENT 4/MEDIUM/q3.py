
#NAYAK DEV_240280117049

d1 = {}
d2 = {}

n1 = int(input("Enter number of elements in first dictionary: "))
for _ in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

n2 = int(input("Enter number of elements in second dictionary: "))
for _ in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

merged = {**d1, **d2}
print("Merged Dictionary:", merged)



