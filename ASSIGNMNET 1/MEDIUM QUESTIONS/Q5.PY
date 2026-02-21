# 240280117049 NAYAK DEV AND 240280117071 PATEL MANAV
# Electricity Bill using reverse slab logic

units = float(input("Enter electricity units consumed: "))

bill = 0


if units > 300:
    bill += (units - 300) * 10
    units = 300


if units > 200:
    bill += (units - 200) * 5
    units = 200


if units > 100:
    bill += (units - 100) * 3
    units = 100


bill += units * 2

print(f"YOUR ELECTRICITY BILL = Rs. {bill:.2f}")