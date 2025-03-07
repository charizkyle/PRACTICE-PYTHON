#BATCH 1
print("Program 1: Bigger Number between 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("\nThe bigger number is", num1)
elif num2 > num1:
    print("\nThe bigger number is", num2)
else:
    print("\nBoth numbers are equal.")


print()
print("Program 2: Equal Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print("\nEqual")
else:
    print("\nNot Equal")


print()
print("Program 3: Sum of 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
print()
print("Sum of the two numbers:", sum)


print()
print("Program 4: Product of 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

prod = num1 * num2
print()
print("Product of the two numbers:", prod)


print()
print("Program 5: Quotient of 2 Numbers")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    quotient = num1 / num2
    print()
    print(f"The quotient is {quotient:.2f}")


print()
print("Program 6: Exponentiation")
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

result = base ** exponent

print(result)


print()
print("Program 7: Sum of 10 Numbers")
total = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print("\nSum of all numbers:", total)


print()
print("Program 8: Odd Numbers Count")
odd_count = 0
odd_numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    if num % 2 != 0:
        odd_count += 1
        odd_numbers.append(num)
        
print()
print(odd_count, "odd numbers")
print(odd_numbers)


print()
print("Program 9: Even Numbers starting from 0-100")

for num in range(101): 
    if num % 2 == 0:
        print(num)


print()
print("Program 10: 0-100 without ending in zero")

for num in range(101): 
    if num % 10 != 0:
        print(num)