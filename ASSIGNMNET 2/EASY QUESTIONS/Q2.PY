#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to print even numbers between two given numbers
A= int(input("Enter starting number: "))
B= int(input("Enter ending number: "))


for i in range(A, B + 1):
    if i % 2 == 0:    
        print(i)

print(f"Even numbers between {A} to {B} are : ")