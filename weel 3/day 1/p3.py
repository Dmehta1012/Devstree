def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    while True:
        print("\n--- Recursive Calculator ---")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice == "2":
            num = int(input("Enter a number: "))
            print(f"Fibonacci of {num} is: {fibonacci(num)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
