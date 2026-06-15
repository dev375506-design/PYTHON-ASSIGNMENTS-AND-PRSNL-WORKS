list1 = [1, 2, 3, 4]
list2 = [3, 5, 6, 7]

common = False

for i in list1:
    if i in list2:
        common = True
        break

print("Have common element:", common)