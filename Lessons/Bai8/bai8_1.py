name = input("Enter you name: ")
with  open("hello.txt", "w", encoding= "utf-8") as f:
    f.write("Hello " + name + "\n")
    f.write("Welcome to Python file handling.")
    f.close()