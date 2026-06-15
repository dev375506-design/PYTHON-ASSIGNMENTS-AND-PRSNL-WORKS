# Create & write file
with open("sample.txt", "w") as f:
    f.write("Hello Dev\n")
    f.write("This is file handling example\n")

# Append data
with open("sample.txt", "a") as f:
    f.write("Appending new line\n")

# Read file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)