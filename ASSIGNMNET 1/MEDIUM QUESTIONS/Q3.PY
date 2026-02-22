# 240280117049 NAYAK DEV 
# Program to calculate grade based on percentage

print("Enter marks of 5 subjects:")

a = float(input("Subject 1: "))
b = float(input("Subject 2: "))
c = float(input("Subject 3: "))
d = float(input("Subject 4: "))
e = float(input("Subject 5: "))

# Percentage
percentage = (a + b + c + d + e) / 5

print(f"Your percentage is {percentage}%")

# THIS BOCK WILL CHECK IF ANY SUBJECTIVE MARKS ARE BELOW 33 OR NOT AND THEN CALCULATE GRADE BASED ON PERCENTAGE
if a < 33 or b < 33 or c < 33 or d < 33 or e < 33:
    grade = "FAIL AS SUBJECTIVE CUTOFF IS NOT CLEARED 😞"

else:
    if percentage >= 90:
        grade = "A+ EXCELLENT 🙂"
    elif percentage >= 75:
        grade = "A GOOD 🙂"
    elif percentage >= 60:
        grade = "B YOU CAN DO BETTER 🙂"
    elif percentage >= 50:
        grade = "C NEED TO IMPROVE 🙂"
    else:
        grade = "FAIL WITH F GRADE L🙂"

print(f"YOU HAVE GOT {grade} AS YOUR PERCENTAGE ARE {percentage}%")
