f = open("students.txt", "r", encoding="utf-8")
for ct in f:
    print("Student: ", ct)
f.close()