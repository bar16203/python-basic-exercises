import csv
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Email"])
    writer.writerow(["Thanh", 21, "thanh@example.vn"])
    writer.writerow(["Linh", 20, "linh@example.vn"])
    writer.writerow(["Kha", 27, "kha@example.vn"])