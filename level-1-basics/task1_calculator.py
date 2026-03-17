# Task: build a calculator that takes two numbers
# and performs +, -, *, /
# Skills: variables, input(), if/elif, basic math

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/" and num2 != 0:
    print(f"Result: {num1 / num2}")
else:
    print("Invalid input or division by zero")    