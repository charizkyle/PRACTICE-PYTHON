#BATCH 2
print("Program 1: Smaller Number between 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 < num2:
    print("\nThe smaller number is", num1)
elif num2 < num1:
    print("\nThe smaller number is", num2)
else:
    print("\nBoth numbers are equal.")


print()
print("Program 2: Not Equal Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 != num2:
    print("\nNot Equal")
else:
    print("\nEqual")


print()
print("Program 3: Difference of 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

diff = num1 - num2
print()
print("Difference of the two numbers:", diff)


print()
print("Program 4: Quotient of 2 Numbers without Decimal")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    quotient = int(num1 / num2)
    print()
    print(f"The quotient is", quotient)


print()
print("Program 5: Remainder")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    rem = num1 % num2
    print()
    print("The remainder is", rem)
    
    
print()
print("Program 6: 1st Number Subtract Rest")
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
    
result = numbers[0] - sum(numbers[1:])
print()
print(result)


print()
print("Program 7: Even Numbers Count")
even_count = 0
even_numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    if num % 2 == 0:
        even_count += 1
        even_numbers.append(num)
        
print()
print(even_count, "odd numbers")
print(even_numbers)


print()
print("Program 8: Odd Numbers starting from 0-100")
num = 1
while num <= 100:
    print(num)
    num += 2


print()
print("Program 9: 0-100 without ending in zero/five")
num = 0
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1


print()
print("Program 10: Numbers between numbers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    num1, num2 = num2, num1

print("Numbers between", num1, "and", num2, "are:")
for num in range(num1 + 1, num2):
    print(num)