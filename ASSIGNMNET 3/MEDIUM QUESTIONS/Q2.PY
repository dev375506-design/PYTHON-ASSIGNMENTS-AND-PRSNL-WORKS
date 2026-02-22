#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV
# Program to count frequency of an element

numbers = [10, 20, 30, 20, 40, 20, 50]

element = int(input("Enter element to count: "))

frequency = numbers.count(element)

print("List:", numbers)
print(f"Frequency of {element} in the list = {frequency}")
