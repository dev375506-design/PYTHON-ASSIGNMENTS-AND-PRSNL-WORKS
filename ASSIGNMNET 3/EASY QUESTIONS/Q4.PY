#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV
# Program to count vowels in a string

text = input("Enter a string: ").lower()

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print(f"Number of vowels in the string = {count}")
