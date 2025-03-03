print("Program 7: Sum of 10 Numbers")
total = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num

print("\nSum of all numbers:", total)