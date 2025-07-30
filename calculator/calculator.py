import calculator_art

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    calculator_art.print_ascii_calculator()

    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        while True:
            print("\nAvailable operations:")
            for symbol in operations:
                print(f"  {symbol}")

            op_symbol = input("Choose an operator: ")
            if op_symbol not in operations:
                print("Invalid operator. Please choose a valid one.")
                continue

            try:
                num2 = float(input("Enter the next number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            operation_func = operations[op_symbol]
            result = operation_func(num1, num2)

            if result is not None:
                print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
            else:
                break

            choice = input("\nType 'y' to continue calculating with the result, 'n' to start over, or 'q' to quit: ").lower()

            if choice == 'y':
                num1 = result
            elif choice == 'n':
                break  # restart outer loop
            elif choice == 'q':
                print("Goodbye!")
                return
            else:
                print("Invalid input. Exiting.")
                return

calculator()
