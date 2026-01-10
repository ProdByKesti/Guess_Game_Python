import random                                                                                       # For using random generated numbers

def give_hints(secret, guess):                                                                      # Function for helpfull hints
    if secret % 2 == 0:                                                                             # deviding the secret number by 2 and if there is no remainder it means that the secret number is even 
        print("The number we are looking for is even")
    else:                                                                                           # Otherwise its an odd number
        print("The number we are looking for is odd")
    
    distance = abs(secret - guess)                                                                  # Subtracting the secret number by the guess, removing the (-) sign and stroing it in the variable distance
    if distance <= 2:                                                                               # If the distance between secret and guess is only two numbers it shows the message in the next line                                                      
        print("Hot")
    elif distance <= 5:
        print("Warm")
    else:
        print("Cold")

    if guess < secret:                                                                              # These hints show if the guess made is lower or higher than the secret number
        print("Too low")
    elif guess > secret:
        print("Too high")

def play_round(min_num, max_num, max_attempts):                                                     # Function for one round
    secret = random.randint(min_num, max_num)                                                       # Creates a random number in the range of min_num(minimal Number) and max_num(maximum number)
    attempts = max_attempts                                                                         # Storing the max attempts from the difficulty menu into another variable

    while attempts > 0:                                                                             # Loops as long as attempts are left
        guess_input = input(f"Guess a Number ({min_num}-{max_num}): ")                              # Main question of the game is also showing the range the player chose 

        if not guess_input.isdigit():                                                               # checking if the guess is a valid number 
            print("Please enter a valid number.")
            continue                                                                                # Asking main question again if the guess is not a valid number 

        guess = int(guess_input)                                                                    # Storing the guess as an integer

        if guess < min_num or guess > max_num:                                                      # Testing if the guess was made outside the playable range
            print(f"Number must be between {min_num} and {max_num}.")                               # Notification about the invalid input
            continue                                                                                # Looping this until a valid input was made

        if guess == secret:                                                                         # Testing if the guess was right
            print("You win!")                                                                       # Notification about the round win
            return True                                                                             # Round won
        print("Wrong guess!")                                                                       # If the guess was wrong the test aove is being skipped
        give_hints(secret, guess)                                                                   # Hints from the give_hints function are shown

        attempts -= 1                                                                               # Taking away 1 attempt after round loss
        print(f"Attempts left: {attempts}")                                                         # Showing the player how many attempts are left 

    print(f"You lost! The number was {secret}")                                                     # Notification that shows as soon as no attempts are left
    return False                                                                                    # ROund lost

def choose_difficulty():                                                                            # Function for choosing difficulty
    while True:                                                                                     # This Loop is only there if the player types in a wron mode
        choice = input("Choose difficulty (easy/medium/hard)").lower()                              # User chooses the difficulty and the .lower() fuction handles makes every input written small

        if choice == "easy":                                                                    
            return 1, 10, 5                                                                         # Returning min_num, max_num and attempts for the chosen difficulty
        elif choice == "medium":
            return 1, 20, 4
        elif choice == "hard":
            return 1, 50, 3
        else:
            print("Invalid difficulty.")                                                            # Message that the input is not readable and jumping back to the start of this fuctions loop


total_rounds = 0                                                                                    # Amount of total ronds to play
                                                                                 
while total_rounds < 1:                                                                             # Making sure the player decides how long they want to play
                                                                                 
    user_input1 = input("How many rounds do you want to play?: ")                                   # Player can decide how many rounds he/she plays

    if not user_input1.strip().isdigit():                                                           # Making sure the input is an integer
        print("Please enter a valid number")                                                        # Info that the game needs an integer to start
        continue                                                                                    # Looping this until an integer was entered

    total_rounds = int(user_input1)                                                                 # Copying the user input to the int total rounds

min_num, max_num, attempts = choose_difficulty()                                                    # Filling variables with infos from chosen difficulty

wins = 0                                                                                            # Counter to later display won rounds

for round_number in range(1, total_rounds + 1):                                                     # Creating a loop for every round 
    print(f"\n---Round {round_number}---")                                                          # Displaying the current round
    if play_round(min_num, max_num, attempts):                                                      # Starting the round function 
        wins +=1                                                                                    # If the round function returns True it will add one win to the score

print(f"\nGame over! You won {wins} out of {total_rounds} Rounds.")                                 # Game end notification shows how many rounds were one 