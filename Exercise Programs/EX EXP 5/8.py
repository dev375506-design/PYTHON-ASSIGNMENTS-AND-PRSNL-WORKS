d = {1: 50, 2: 20, 3: 40, 4: 10}

print("Original dictionary:", d)

sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_dict)