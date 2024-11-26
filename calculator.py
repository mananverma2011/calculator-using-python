print("Hello! Welcome to the calculator app")
print("Today I have made a calculator app as a beginner project!")

int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))
operation = input("Enter the operation to be performed. type * to multiply, / to divide, + to add, - to subtract. ")

if operation == "*":
    print(f"The product of the number is: {int1 * int2}")
elif operation == "/":
    print(f"The quotient of the numbers is: {int1 / int2}")
elif operation == "+":
    print(f"The sum of the following numbers is: {int1 + int2}")
elif operation == "-":
    print(f"The difference of the following numbers is: {int1 - int2}")
else:
    print("That's not a valid input. Remember there is no s in subtracting!")