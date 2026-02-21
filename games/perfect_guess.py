import random
n=random.randint(1,100)
a=-1
guesess=1
while(a!=n):
    a=int(input("Enter your guess: "))
    if(a>n):
        print("Too high! Try again.")
    elif(a<n):
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {n} in {guesess} guesses.")
    guesess+=1
print(f"Congratulations! You've guessed the number {n} in {guesess-1} guesses.")