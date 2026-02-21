fruits = []

def adding():
    while True:
        choice = input("Do you want to add a fruit? (yes/no): ").lower()
        if choice == "yes":
            fruit = input("Enter your fruit: ")
            fruits.append(fruit)
        else:
            break

adding()

print("Your fruits list:", fruits)
