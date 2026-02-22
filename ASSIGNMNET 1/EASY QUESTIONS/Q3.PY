# 240280117049 NAYAK DEV 
# Celsius to Fahrenheit using function

def c_to_f(c):
    f = (c * 9/5) + 32
    return f

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = c_to_f(celsius)

print("Temperature in Fahrenheit =", fahrenheit)