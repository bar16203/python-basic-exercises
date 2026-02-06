import csv 
numberOfStudents = int(input("Enter number of students: "))
#students = []
for i in range(numberOfStudents):
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    email = input("Enter student email: ")
    student = [name, age, email]
    with open("students.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(student)