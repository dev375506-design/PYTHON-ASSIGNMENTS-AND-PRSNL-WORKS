import random 

def play():
    options = ["stone", "paper", "scissors"]
    user_choice = input("Choose stone, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
play()
