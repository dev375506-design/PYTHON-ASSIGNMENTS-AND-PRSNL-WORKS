r1 = float(input("Enter first resistance: "))
r2 = float(input("Enter second resistance: "))

series = r1 + r2
parallel = (r1 * r2) / (r1 + r2)

print("Series resistance:", series)
print("Parallel resistance:", parallel)