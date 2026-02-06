a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
operation = input("Enter operation: ")
if operation == '+':
    print("Your result: ", a + b)
elif operation == '-':
    print("Your result: ", a - b)
elif operation == '*':
    print("Your result: ", a * b)
elif operation == '/':
    print("Your result: ", a / b)
else:
    print("Please enter calculation.")
