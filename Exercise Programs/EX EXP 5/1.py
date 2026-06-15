lst = []

for i in range(5):
    x = int(input("Enter element: "))
    lst.append(x)

print("List:", lst)
print("First 3 elements:", lst[:3])

lst.pop()
print("After removing last:", lst)