import pandas as pd

data = {
    "Name": ["Dev", "Raj", "Amit"],
    "Marks": [85, 60, 75]
}

df = pd.DataFrame(data)

# Add column
df["Grade"] = ["A", "C", "B"]
print("After adding column:\n", df)

# Delete column
df.drop("Grade", axis=1, inplace=True)
print("After deleting column:\n", df)