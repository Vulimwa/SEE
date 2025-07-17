num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation."  

print("Result:", result)
with open("result.txt", "w") as file:
    file.write(str(result))
print("Result saved to result.txt")
# calculator.py
# calculator.py
# This script performs basic arithmetic operations and saves the result to a file.