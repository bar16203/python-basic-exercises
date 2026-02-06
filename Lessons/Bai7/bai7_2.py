students = [
    {
        "name" : "A",
        "age" : 20
    },
    {
        "name" : "B",
        "age" : 22
    },
    {
        "name" : "C",
        "age" : 19
    }
]
total = 0
for st in students: 
    total += st["age"]
print("Total Age:", total)