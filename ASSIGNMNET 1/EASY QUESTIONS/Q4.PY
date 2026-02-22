#240280117049 NAYAK DEV AND 240280117071 PATEL MANAV

# Program to calculate area of a rectangle


length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

def area_of_rectangle(length, breadth):
    return length * breadth

area = area_of_rectangle(length, breadth)
print(f"Area of the rectangle  = {area}")