import matplotlib.pyplot as plt

items = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]

plt.bar(items, values)
plt.xlabel("Items")
plt.ylabel("Values")
plt.title("Bar Chart")

plt.show()