#NAYAK DEV_240280117049

import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = []

for sub in subjects:
    m = int(input(f"Enter marks for {sub}: "))
    marks.append(m)

plt.plot(subjects, marks, marker='o')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks in 5 Subjects")
plt.grid()

plt.show()