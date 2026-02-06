name = input("Enter new name: ")
f = open("students.txt", "a", encoding="utf-8")
f.write(name + "\n")