# Function for the basic calculator
def calculator():
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter your choice (1/2/3/4): ")
    
    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
        
    elif operation == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
        
    elif operation == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
        
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
            
    else:
        print("\nInvalid operation choice.")

# Run the calculator
calculator()
