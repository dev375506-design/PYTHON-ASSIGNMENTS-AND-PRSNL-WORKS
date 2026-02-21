# 240280117049 NAYAK DEV AND 240280117071 PATEL MANAV
# Program to calculate grade based on percentage

print("Enter marks of 5 subjects:")

a = float(input("Subject 1: "))
b = float(input("Subject 2: "))
c = float(input("Subject 3: "))
d = float(input("Subject 4: "))
e = float(input("Subject 5: "))

# Percentage
percentage = (a + b + c + d + e) / 5

print("\nPercentage =", percentage, "%")

# Check fail in any subject
if a < 33 or b < 33 or c < 33 or d < 33 or e < 33:
    grade = "FAIL"

else:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "FAIL"

print(f"YOU HAVE GOT {grade} AS YOUR PERCENTAGE ARE {percentage}%")
