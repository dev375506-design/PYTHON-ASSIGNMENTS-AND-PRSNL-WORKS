import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Multiple Line Plot")

plt.show()