class InvalidOperatorError(Exception):
    pass

def cal():
    print("Welcome to Calculator")
    print("Supported Operators: '+', '-', '*', '/', '**', '%'")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        try:
            
            num1_input = input("Enter Num1: ")
            if num1_input.lower() == "exit":
                print("Goodbye!")
                break
            num1 = float(num1_input)

            
            op = input("Enter your Operator: ").strip()
            if op.lower() == "exit":
                print("Goodbye!")
                break
            if op not in ['+', '-', '*', '/', '**', '%']:
                raise InvalidOperatorError(f"'{op}' is invalid.")

            
            num2_input = input("Enter Num2: ")
            if num2_input.lower() == "exit":
                print("Goodbye!")
                break
            num2 = float(num2_input)

            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Number cannot be divided by zero!")
                result = num1 / num2
            elif op == '**':
                result = num1 ** num2
            elif op == '%':
                if num2 == 0:
                    raise ZeroDivisionError("Modulo by zero is not allowed!")
                result = num1 % num2

            print(" Result:", result, "\n")

        except ValueError:
            print(" Invalid value! Please enter a number.\n")
        except InvalidOperatorError as e:
            print(f" {e}\n")
        except ZeroDivisionError as zde:
            print(f" {zde}\n")

# Run the calculator
cal()
