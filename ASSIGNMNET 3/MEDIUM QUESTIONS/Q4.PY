#240280117049 NAYAK DEV

# Program to check whether a string is palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")
