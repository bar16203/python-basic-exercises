import csv 
students = [
    {"Name": "Thanh","Age": 21,"Email": "thanh@example.vn"},
    {"Name": "Linh","Age": 21,"Email": "linh@example.vn"},
    {"Name": "Kha","Age": 27,"Email": "kha@example.vn"}
]
fields = ["Name", "Age", "Email"]
with open("students2.csv","w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)