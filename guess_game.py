import random                                       # For using random generated numbers

secret = random.randint(1, 10)                      # Generating a new random number for every Match
attempts = 3                                        # Amount of Attempts

print("Guess the number (1-10)")                    # Instructions for the player 


while attempts > 0:                                 # Loop Starts only if there are 1 or more attempts left 
    user_input = input("Your guess: ")              # Taking the first input of the player 

    if not user_input.strip().isdigit():            # checking if the input is an integer 
        print("Please enter a valid number")        # Asking for another input
        continue                                    # Jumping back to the start of the loop

    guess = int(user_input)                         # Transferring the user input to a better readable integer

    if guess < 1 or guess > 10:                     # Checking if the input is in the printed range of the game
        print("Number must be between 1 and 10")    # Reminder that the number has to be between 1 and 10       
        continue                                    # Jumping back to the start of the loop

    if guess == secret:                             # Checking if the guess is equal to the randomly generated secret number
        print("Congrats!! You win!")                # Little notification so the player knows that he/she won
        break                                       # Stopping the loop/game
    elif guess < secret:                            # Checking if the guess is lower then the randomly generated secret number
        print("Too low!")                           # Little notification to inform the player about their guess
    else:                                           # Checking if the guess is greater then the randomly generated secret number
        print("Too high!")                          # Little notification to inform the player about their guess

    attempts -= 1                                   # Removing one attempt after each guess until it reaches zero
    print("Attempts left:", attempts)               # Reminder of how many attempts are left 

if attempts == 0:                                   # Checking how many attempts are left since while loop is not running anymore
    print("Game Over! The number was:", secret)     # Giving a end of the game notification