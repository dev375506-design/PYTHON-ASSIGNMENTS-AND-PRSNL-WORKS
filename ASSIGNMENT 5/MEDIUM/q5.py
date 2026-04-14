#NAYAK DEV_240280117049

import pandas as pd

n = int(input("Enter number of records: "))
data = []

for _ in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    data.append({"Roll": roll, "Name": name, "Marks": marks})

df = pd.DataFrame(data)

print("\nFull DataFrame:\n", df)

print("\nFirst Row:\n", df.iloc[0])

print("\nMarks Column:\n", df["Marks"])

print("\nStudents with marks > 50:\n", df[df["Marks"] > 50])