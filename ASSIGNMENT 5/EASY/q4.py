#NAYAK DEV_240280117049

import pandas as pd

data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

series = pd.Series(data)

print("Full Series:\n", series)
print("Access element with index 'b':", series["b"])
print("Slicing (first 2 elements):\n", series[:2])