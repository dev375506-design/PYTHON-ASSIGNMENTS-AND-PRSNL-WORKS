#240280117049 NAYAK DEV 

# Program to check whether a year is leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")

elif year % 100 == 0:
    print(year, "is NOT a Leap Year")

elif year % 4 == 0:
    print(year, "is a Leap Year")

else:
    print(year, "is NOT a Leap Year")