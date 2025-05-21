#Adding numbers*
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The total is:", num1 + num2)
except ValueError:
    print("Oops! That was not a valid number. Please enter numbers only.")
