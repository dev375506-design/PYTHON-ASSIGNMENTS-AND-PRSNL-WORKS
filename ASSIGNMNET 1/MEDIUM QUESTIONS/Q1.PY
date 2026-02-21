#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to check whether a year is leap year

year = int(input("Enter a year: "))

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
