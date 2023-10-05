# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers to find the smaller one
if num1 < num2:
    print(f"{num1} is smaller than {num2}.")
elif num1 > num2:
    print(f"{num2} is smaller than {num1}.")
else:
    print("Both numbers are equal.")
