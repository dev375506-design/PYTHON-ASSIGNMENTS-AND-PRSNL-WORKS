#240280117049 NAYAK DEV 

# Program to count vowels in a string

text = input("Enter a string: ").lower()

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(f"Number of vowels in the string = {count}")
