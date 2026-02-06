students = ["Thanh", "Nam", "Linh", "Tú"]
with open("students.txt", "w", encoding="utf-8") as f:
    for st in students:
        f.write(st + "\n")