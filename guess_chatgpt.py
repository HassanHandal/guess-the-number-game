import random

user_name = input("Hello, let's play a guessing game. What's your name?:\n")
attempts = []

while True:
    print(f"There {'is no high score yet' if not attempts else f'is currently a high score of {min(attempts)}. Try to break it.'}")

    try:
        user_choice = int(input(f"{user_name}, guess the number I have chosen. It must be from 1 to 10:\n"))
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    pc_random = random.randint(1, 10)
    attemp_no = 1

    while user_choice != pc_random:
        attemp_no += 1
        user_choice = int(input(f"No {user_name}, it is {'smaller' if user_choice > pc_random else 'greater'} than your guess. Enter a {'smaller' if user_choice > pc_random else 'greater'} number:\n"))

    attempts.append(attemp_no)
    print(f"Eureka! You guessed the right number, {user_name}, and you used {attemp_no} attempts.")

    ask = input("Do you want to play again? (Y/N):\n").lower()
    while ask not in ["n", "y"]:
        ask = input("Enter an available choice (Y/N):\n").lower()

    if ask == "n":
        break
