def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            # Get user input
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operator
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator! Please use +, -, *, or /")
                continue
                
            # Display result
            print(f"Result: {num1} {op} {num2} = {result}")
            
            # Ask if user wants to continue
            again = input("Calculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            
if __name__ == "__main__":
    calculator()