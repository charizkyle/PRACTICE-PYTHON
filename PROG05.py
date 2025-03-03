print("Program 5: Quotient of 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("Division by zero is UNDEFINED.")

quotient = num1 / num2
print()
print(f"The quotient is {quotient:.2f}")