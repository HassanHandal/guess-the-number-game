import random
from check_integer import check_int

user_name = input("Hello, let's play a guessing game. What's your name?:\n")
attempts = []

while True:
    pc_random = str(random.randint(1, 10))
    user_choice = check_int(input(f"{user_name}, guess the number I've chosen between 1 and 10:\n"))
    
    attemp_no = 1

    while user_choice != pc_random:
        attemp_no += 1
        user_choice = check_int(input(f"No {user_name}, it's {'smaller' if user_choice > pc_random else 'greater'} than your choice. Guess again:\n"))

    attempts.append(attemp_no)
    print(f"Eureka, you guessed the right number, {user_name}, in {attemp_no} attempts")

    ask = input("Do you want to play again? Y/N:\n").lower()
    
    while ask not in ["n", "y"]:
        ask = input("Enter an available choice:\n")

    if ask == "n":
        break

if not attempts:
    print("Thanks for playing!")
else:
    high_score = min(attempts)
    print(f"The current high score is {high_score}. Thanks for playing!")
