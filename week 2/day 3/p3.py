import random

name = input("Enter your name: ").upper()
print(f"Hello {name}\nWinning Rules:\nRock vs Paper -> Paper wins\nRock vs Scissor -> Rock wins\nPaper vs Scissor -> Scissor wins.\n")

while True:
    choice = int(input("Enter your choice (1=Rock, 2=Paper, 3=Scissor): "))
    while choice < 1 or choice > 3:
        choice = int(input("Enter a valid choice (1‑3): "))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"

    print(f"{name} choice: {choice_name}")
    print("Computer's turn...")

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    print(f"Computer choice: {comp_choice_name}")
    print(f"{choice_name} vs {comp_choice_name}")

    if choice == comp_choice:
        result = "Draw"
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = "Rock"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = "Paper"
    else:
        result = "Scissor"

    if result == "Draw":
        print("It's a tie!")
    elif result == choice_name:
        print(f"{name} wins!")
    else:
        print("Computer wins!")

    if input("Do you want to play again? (y/n): ").lower() == 'n':
        break

print("Thanks for playing!")


