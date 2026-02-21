#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to print even numbers between two given numbers

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))


for i in range(start, end + 1):
    if i % 2 == 0:     # check even
        print(i)

print(f"Even numbers between {start} to {end} are : ")