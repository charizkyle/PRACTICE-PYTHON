print("Program 1: Bigger Number between 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("\nThe bigger number is", num1)
elif num2 > num1:
    print("\nThe bigger number is", num2)
else:
    print("\nBoth numbers are equal.")