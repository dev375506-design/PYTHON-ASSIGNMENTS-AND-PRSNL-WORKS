p = float(input("Enter principal: "))
r = float(input("Enter rate (%): "))
t = float(input("Enter time (years): "))

# Simple Interest
si = (p * r * t) / 100

# Compound Interest
ci = p * (1 + r/100) ** t - p

print("Simple Interest:", si)
print("Compound Interest:", ci)