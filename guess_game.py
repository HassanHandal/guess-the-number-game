import random
from check_integer import check_int
pc_random = str(random.randint(1,10))
user_name = input("Hello, let's play a guess number, what's your name?:\n")
attempts = []
while True:
    if not attempts:
        print("There is no high score yet")
    else:
        high_score = min(attempts)
        print(f"The currently high score is {high_score}, try to break it")
    user_choice = input(f"{user_name}, guess the number I have chosen. Take care, it must be from 1 to 10:\n")
    check_int(user_choice)
    attemp_no = 1
    while user_choice != pc_random:
        attemp_no = attemp_no + 1
        if user_choice > pc_random:
            user_choice = input(f"No {user_name}, It is smaller than your choice guess a smaller number:\n")
            check_int(user_choice) 
        elif user_choice < pc_random:
            user_choice = input(f"No {user_name}, It is greater than your choice guess a greater number:\n")
            check_int(user_choice)        
    attempts.append(attemp_no)
    print(f"Eureka, you guessed the right number, {user_name}, you have used {str(attemp_no)} attempts")
    ask = input("Do you need to play again? Y/N:\n".lower())
    while ask not in ["n","y"]:
        ask =input("enter an available choice:\n")    
    if ask == "n":
        break




