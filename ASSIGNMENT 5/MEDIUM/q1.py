#NAYAK DEV_240280117049
import csv

n = int(input("Enter number of students: "))

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Marks"])
    
    for _ in range(n):
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        writer.writerow([roll, name, marks])

print("Data written successfully.\n")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)