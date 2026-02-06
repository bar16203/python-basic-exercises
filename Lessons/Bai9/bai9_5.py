import csv 
name = input("Enter the name of the student you are looking for: ")
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: 
        if row[0] == name: 
            print("Name: " + row[0] + ", Age: " + row[1] + ", Email: " + row[2])