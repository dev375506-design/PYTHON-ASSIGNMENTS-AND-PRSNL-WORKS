d = {}

def adding_dict():
    while True:
        choice = input("Do you want to add :(yes/no)? ")
        if choice == "yes":
            key = input("Enter the word: ")
            value = input("Enter its meaning: ")
            d[key] = value   # add to dictionary
        else:
            break

adding_dict()
print("Your dict is:", d)
