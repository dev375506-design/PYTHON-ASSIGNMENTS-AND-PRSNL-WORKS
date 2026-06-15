import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
a = 2

y = [a * i for i in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = a*x")

plt.show()