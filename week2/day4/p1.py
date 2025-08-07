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