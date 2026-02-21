#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to check vowel or consonant

ch = input("Enter a character: ")

# Convert to lowercase
ch = ch.lower()

# Check only alphabet
if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")
else:
    print("Please enter a single alphabet only")
