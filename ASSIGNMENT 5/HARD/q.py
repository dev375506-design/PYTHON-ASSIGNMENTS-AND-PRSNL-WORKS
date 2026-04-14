#NAYAK DEV_240280117049
try:
    filename = input("Enter file name: ")
    
    with open(filename, "r") as file:
        content = file.read()
        print("File Content:\n", content)
    
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    
    result = a / b
    print("Result:", result)

except FileNotFoundError:
    print("Error: File not found.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")