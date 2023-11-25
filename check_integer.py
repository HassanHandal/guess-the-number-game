def check_int(input_user):
    while True:
        try:
            number = int(input_user)
            break
        except ValueError:
            try:
                number = float(input_user)
                print("You entered a float:", number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                input_user = input("Try again:\n")