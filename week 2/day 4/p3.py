while True:
    print("\nThis is Menu \n" \
    "1.Say hello\n" \
    "2.calculator\n" \
    "3.shopping list\n" \
    "4.Number gussing game\n" \
    "5.Quit\n")
    choice=int(input("Enter number from 1-5:-"))

    match choice:
        case 1:
            name=input("Enter your Name ").upper()
            print(f"hello! {name}")
            continue
        case 2:
            print("Welcome to the calculator ")

            num1=int(input("Enter any  num1: "))
            num2=int(input("Enter any  num2:"))
            
            
            print("\n\______________________________________/")
            print("select your choice ")
            print("1 for addition")
            print("2 for subtraction")
            print("3 for multiplication")
            print("4 for divsion\n")
            num=int(input("Enter any from 1 to 4 number: "))
            
            if num==1:
                print("your ans:",num1+num2)
            elif num==2:
                print("your ans:",num1-num2)
            elif num==3:
                print("your ans:",num1*num2)
            elif num==4:
                if num1!=0 and num2!=0:
                    print("your ans:",num1/num2)
                else:
                    print("Can't divisible by zero")
            else:
                print("enter valid choice")
            continue
        case 3:
            shopping_list = []

            while True:
                print("\nShopping List Menu")
                print("1. Add Items")
                print("2. Remove Items")
                print("3. View Items")
                print("4. Exit\n")

                c = input("Enter your choice (1-4): ")

                if c == '1':
                    item = input("Enter item to add: ")
                    shopping_list.append(item)
                    print(f"You added: {item}")

                elif c == '2':
                    if not shopping_list:
                        print("Your shopping list is empty.")
                    else:
                        print("\nYour Shopping List:")
                        for idx, it in enumerate(shopping_list):
                            print(f"{idx + 1}. {it}")
                            r_index = int(input("Enter the number to remove: ")) - 1
                        if 0 <= r_index < len(shopping_list):
                            removed = shopping_list.pop(r_index)
                            print(f"Removed: {removed}")
                        else:
                            print("Invalid number.")

                elif c == '3':
                    if not shopping_list:
                        print("Your shopping list is empty.")
                    else:
                        print("\nYour Shopping List:")
                        for item in shopping_list:
                            print(f"- {item}")

                elif c == '4':
                    print("Goodbye!")
                    break
                
                else:
                    print("Invalid choice, please enter a number from 1 to 4.")
            continue
        case 4:
            print("welcome to  numebr gussing game")
            secret=int(input("enter number to guess:-"))
            print(f"you enter this {secret} number")
            guess=0
            attempts = 0     
            while guess != secret:
                    try:
                        guess = int(input("Your guess: "))
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                        continue
                    
                    attempts += 1

                    if guess < secret:
                        print("Too low — try a higher number.")
                    elif guess > secret:
                        print("Too high — try a lower number.")

            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            print("Game over. Thanks for playing!")
            continue
        case 5:
            print("Goodbye!")
            break
        case _:
            print("Invalid number !Please select from 1-5")
            continue
