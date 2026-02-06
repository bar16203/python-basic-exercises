import csv 
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: 
        print("Name: " + row[0] + ", Age: " + row[1] + ", Email: " + row[2])