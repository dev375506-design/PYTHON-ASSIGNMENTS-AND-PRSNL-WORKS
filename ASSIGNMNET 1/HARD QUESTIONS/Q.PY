#240280117049 NAYAK DEV 
# # Menu Driven Calculator Program

start = input("Do you want to use the calculator? (yes/no): ").lower()

if start == "yes":

    print("\nWhat do you want to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1-4): ")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result =", n1 + n2)

    elif choice == '2':
        print("Result =", n1 - n2)

    elif choice == '3':
        print("Result =", n1 * n2)

    elif choice == '4':
        if n2 == 0:
            print("Error! Division by zero not allowed.")
        else:
            print("Result =", n1 / n2)

    else:
        print("Please choose from 1 to 4 only 🙂")

    print("\nThank you for using my  calculator!")

else:
    print("Okay, maybe next time 😊")