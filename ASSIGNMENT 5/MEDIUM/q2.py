#NAYAK DEV_240280117049

import pickle

numbers = []
n = int(input("Enter number of integers: "))

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

with open("data.bin", "wb") as file:
    pickle.dump(numbers, file)

print("Data stored in binary file.\n")

with open("data.bin", "rb") as file:
    data = pickle.load(file)

print("Data read from file:", data)