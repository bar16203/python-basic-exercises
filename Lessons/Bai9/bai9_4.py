import csv 
countStudent = 0
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: 
        countStudent +=1
print("Total number of students: ", countStudent)