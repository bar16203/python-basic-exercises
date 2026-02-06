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
for st in students:
    if st["age"] >= 21:
        print(st["name"], "is older than 20 years old")