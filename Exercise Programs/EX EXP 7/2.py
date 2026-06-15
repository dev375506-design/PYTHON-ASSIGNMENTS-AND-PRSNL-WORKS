import csv

# Write CSV file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Dev", 85])
    writer.writerow(["Raj", 90])
    writer.writerow(["Amit", 75])

# Read CSV file
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    total = 0
    count = 0

    print("CSV Data:")
    next(reader)  # skip header
    for row in reader:
        print(row)
        total += int(row[1])
        count += 1

# Process data (average)
avg = total / count
print("Average Marks:", avg)