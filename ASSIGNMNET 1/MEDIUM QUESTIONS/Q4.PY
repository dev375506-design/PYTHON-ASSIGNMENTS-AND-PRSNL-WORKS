# 240280117049 NAYAK DEV 
# Program to check vowel or consonant

ch = input("Enter a character: ").lower()

if len(ch) != 1:
    print("Enter only one character")

elif ch in "abcdefghijklmnopqrstuvwxyz":

    if ch in "aeiou":
        print(ch, "is a Vowel")
    else:
        print(ch, "is a Consonant")

else:
    print("Enter an alphabet only")