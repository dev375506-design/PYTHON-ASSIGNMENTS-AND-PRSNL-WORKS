#NAYAK DEV_240280117049

n = int(input("Enter number of students: "))
students = {}

for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (space separated): ").split()))
    students[name] = marks

topper = ""
highest_avg = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(f"{name} Average: {avg:.2f}")
    
    if avg > highest_avg:
        highest_avg = avg
        topper = name

print("Topper:", topper)
print("Highest Average:", round(highest_avg, 2))