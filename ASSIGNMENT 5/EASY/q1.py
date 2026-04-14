#NAYAK DEV_240280117049

with open("data.txt", "w") as file:
    for i in range(1, 6):
        line = input(f"Enter line {i}: ")
        file.write(line + "\n")

print("File created and data written successfully.")