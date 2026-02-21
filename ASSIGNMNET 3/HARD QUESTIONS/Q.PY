# 240280117049 NAYAK DEV AND 
# Second largest element (simple method)

numbers = [12, 45, 7, 23, 89, 34, 89]


largest = max(numbers)


new_list = []
for num in numbers:
    if num != largest:
        new_list.append(num)


if len(new_list) == 0:
    print("Second largest element does not exist")
else:
    second_largest = max(new_list)
    print("List:", numbers)
    print("Largest element =", largest)
    print("Second largest element =", second_largest)