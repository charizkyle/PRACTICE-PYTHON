print("Program 8: Odd Numbers")
odd_num = 0

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    if num % 2 != 0:
        odd_num += 1

print("\nThe number of odd numbers entered is:", odd_num)
