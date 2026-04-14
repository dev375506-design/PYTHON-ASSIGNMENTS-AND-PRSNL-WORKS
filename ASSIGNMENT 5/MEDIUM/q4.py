#NAYAK DEV_240280117049

import numpy as np

arr1 = np.array(list(map(int, input("Enter elements of first array: ").split())))
arr2 = np.array(list(map(int, input("Enter elements of second array: ").split())))

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)