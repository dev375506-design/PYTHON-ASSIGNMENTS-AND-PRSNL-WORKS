import pandas as pd

data = {
    "Name": ["Dev", "Raj", "Amit", "Neha"],
    "Marks": [85, 60, 75, 90]
}

df = pd.DataFrame(data)

filtered = df[df["Marks"] > 70]

print("Filtered Data:\n", filtered)