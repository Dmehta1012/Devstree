shopping_list = []

while True:
    print("\nShopping List Menu")
    print("1. Add Items")
    print("2. Remove Items")
    print("3. View Items")
    print("4. Exit")

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
