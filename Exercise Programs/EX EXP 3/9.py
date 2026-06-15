n = int(input("Enter number (1-7): "))

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
        "FRIDAY", "SATURDAY", "SUNDAY"]

if 1 <= n <= 7:
    print(days[n-1])
else:
    print("Invalid input")