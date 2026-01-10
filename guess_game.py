import random                                                                                       # For using random generated numbers


attempts = 3                                                                                        # Amount of Attempts
rounds_played = 0                                                                                   # Amount of played rounds
total_rounds = 0                                                                                    # Amount of total ronds to play
rounds_won = 0                                                                                      # Amount of rounds won
difficulty = 0                                                                                      

while difficulty == 0:

    user_input2 = input("1:Easy(Numbers from 1-10, 3 attempts)\n" \
                        "2:Medium(Numbers from 1-20, 4 attempts)\n" \
                        "3:Hard(Numbers from 1-50, 5 attempts)\n"
                        "Choose your difficulty")
    
    if not user_input2.strip().isdigit(): 
        print("Please enter a valid number")
        continue

    choice = int(user_input2)

    if choice < 1 or choice > 3:
        print("Please enter a number between 1 and 3")
        continue

    difficulty = choice

    if difficulty == 1:
        print("You chose easy mode")

        while total_rounds < 1:
                                                                                 
            user_input1 = input("How many rounds do you want to play?: ")                           # Player can decide how many rounds he/she plays

            if not user_input1.strip().isdigit():                                                   # Making sure the input is an integer
                print("Please enter a valid number")                                                # Info that the game needs an integer to start
                continue                                                                            # Looping this until an integer was entered

            total_rounds = int(user_input1)                                                         # Copying the user input to the int total rounds

            while rounds_played < total_rounds:                                                     # Looping the game as long as the int for the played rounds is smaller than the total rounds 

                secret = random.randint(1, 10)                                                      # Generating a random number at the start of each round
                print("Guess the number (1-10)")                                                    # Instructions for the player 


                while attempts > 0:                                                                 # Loop Starts only if there are 1 or more attempts left 

                    user_input = input("Your guess: ")                                              # Taking the first input of the player 

                    if not user_input.strip().isdigit():                                            # checking if the input is an integer 
                        print("Please enter a valid number")                                        # Asking for another input
                        continue                                                                    # Jumping back to the start of the loop

                    guess = int(user_input)                                                         # Transferring the user input to a better readable integer

                    if guess < 1 or guess > 10:                                                     # Checking if the input is in the printed range of the game
                        print("Number must be between 1 and 10")                                    # Reminder that the number has to be between 1 and 10       
                        continue                                                                    # Jumping back to the start of the loop

                    if guess == secret:                                                             # Checking if the guess is equal to the randomly generated secret number
                        print(f"Congrats!! {secret} was the right number! You win!")                # Little notification so the player knows that he/she won
                        rounds_played += 1                                                          # Adding one to the played rounds
                        print(f"Rounds played {rounds_played} out of {total_rounds}")               # Notification for the player
                        rounds_won += 1                                                             # Adding one to the rounds won
                        attempts = 3                                                                # resetting the attempts 
                        break                                                                       # Stopping the loop/game

                    elif guess < secret:                                                            # Checking if the guess is lower then the randomly generated secret number
                        print("Too low!")                                                           # Little notification to inform the player about their guess

                    else:                                                                           # Checking if the guess is greater then the randomly generated secret number
                        print("Too high!")                                                          # Little notification to inform the player about their guess

                    attempts -= 1                                                                   # Removing one attempt after each guess until it reaches zero
                    print("Attempts left:", attempts)                                               # Reminder of how many attempts are left 

                if attempts == 0:                                                                   # Checking how many attempts are left since while loop is not running anymore
                    print("Game Over! The number was:", secret)                                     # Giving a end of the game notification
                    rounds_played += 1                                                              # Adding one to the rounds played
                    print("Rounds played:", rounds_played)                                          # Notification for the player
                    attempts = 3                                                                    # Resetting the attempts
                    
            if rounds_played == total_rounds:                                                       # checking if all srounds were played
                print(f"You won {rounds_won} round(s) out of {rounds_played}")                      # End result

    elif difficulty == 2:
        print("you chose medium mode")
        attempts = 4

        while total_rounds < 1:                                                                     

            user_input1 = input("How many rounds do you want to play?: ")                           # Player can decide how many rounds he/she plays

            if not user_input1.strip().isdigit():                                                   # Making sure the input is an integer
                print("Please enter a valid number")                                                # Info that the game needs an integer to start
                continue                                                                            # Looping this until an integer was entered

            total_rounds = int(user_input1)                                                         # Copying the user input to the int total rounds

            while rounds_played < total_rounds:                                                     # Looping the game as long as the int for the played rounds is smaller than the total rounds 

                secret = random.randint(1, 20)                                                      # Generating a random number at the start of each round
                print("Guess the number (1-20)")                                                    # Instructions for the player 

                while attempts > 0:                                                                 # Loop Starts only if there are 1 or more attempts left 

                    user_input = input("Your guess: ")                                              # Taking the first input of the player 

                    if not user_input.strip().isdigit():                                            # checking if the input is an integer 
                        print("Please enter a valid number")                                        # Asking for another input
                        continue                                                                    # Jumping back to the start of the loop

                    guess = int(user_input)                                                         # Transferring the user input to a better readable integer

                    if guess < 1 or guess > 20:                                                     # Checking if the input is in the printed range of the game
                        print("Number must be between 1 and 20")                                    # Reminder that the number has to be between 1 and 10       
                        continue                                                                    # Jumping back to the start of the loop

                    if guess == secret:                                                             # Checking if the guess is equal to the randomly generated secret number
                        print(f"Congrats!! {secret} was the right number! You win!")                # Little notification so the player knows that he/she won
                        rounds_played += 1                                                          # Adding one to the played rounds
                        print(f"Rounds played {rounds_played} out of {total_rounds}")               # Notification for the player
                        rounds_won += 1                                                             # Adding one to the rounds won
                        attempts = 4                                                                # resetting the attempts 
                        break                                                                       # Stopping the loop/game

                    elif guess < secret:                                                            # Checking if the guess is lower then the randomly generated secret number
                        print("Too low!")                                                           # Little notification to inform the player about their guess

                    else:                                                                           # Checking if the guess is greater then the randomly generated secret number
                        print("Too high!")                                                          # Little notification to inform the player about their guess

                    attempts -= 1                                                                   # Removing one attempt after each guess until it reaches zero
                    print("Attempts left:", attempts)                                               # Reminder of how many attempts are left 

                if attempts == 0:                                                                   # Checking how many attempts are left since while loop is not running anymore
                    print("Game Over! The number was:", secret)                                     # Giving a end of the game notification
                    rounds_played += 1                                                              # Adding one to the rounds played
                    print("Rounds played:", rounds_played)                                          # Notification for the player
                    attempts = 4                                                                    # Resetting the attempts

            if rounds_played == total_rounds:                                                       # checking if all srounds were played
                print(f"You won {rounds_won} round(s) out of {rounds_played}")                      # End result

    elif difficulty == 3:
        print("you chose hard mode")
        attempts = 5

        while total_rounds < 1:                        

            user_input1 = input("How many rounds do you want to play?: ")                           # Player can decide how many rounds he/she plays

            if not user_input1.strip().isdigit():                                                   # Making sure the input is an integer
                print("Please enter a valid number")                                                # Info that the game needs an integer to start
                continue                                                                            # Looping this until an integer was entered

            total_rounds = int(user_input1)                                                         # Copying the user input to the int total rounds

            while rounds_played < total_rounds:                                                     # Looping the game as long as the int for the played rounds is smaller than the total rounds 

                secret = random.randint(1, 50)                                                      # Generating a random number at the start of each round
                print("Guess the number (1-50)")                                                    # Instructions for the player 


                while attempts > 0:                                                                 # Loop Starts only if there are 1 or more attempts left 

                    user_input = input("Your guess: ")                                              # Taking the first input of the player 

                    if not user_input.strip().isdigit():                                            # checking if the input is an integer 
                        print("Please enter a valid number")                                        # Asking for another input
                        continue                                                                    # Jumping back to the start of the loop

                    guess = int(user_input)                                                         # Transferring the user input to a better readable integer

                    if guess < 1 or guess > 50:                                                     # Checking if the input is in the printed range of the game
                        print("Number must be between 1 and 50")                                    # Reminder that the number has to be between 1 and 10       
                        continue                                                                    # Jumping back to the start of the loop

                    if guess == secret:                                                             # Checking if the guess is equal to the randomly generated secret number
                        print(f"Congrats!! {secret} was the right number! You win!")                # Little notification so the player knows that he/she won
                        rounds_played += 1                                                          # Adding one to the played rounds
                        print(f"Rounds played {rounds_played} out of {total_rounds}")               # Notification for the player
                        rounds_won += 1                                                             # Adding one to the rounds won
                        attempts = 5                                                                # resetting the attempts 
                        break                                                                       # Stopping the loop/game

                    elif guess < secret:                                                            # Checking if the guess is lower then the randomly generated secret number
                        print("Too low!")                                                           # Little notification to inform the player about their guess

                    else:                                                                           # Checking if the guess is greater then the randomly generated secret number
                        print("Too high!")                                                          # Little notification to inform the player about their guess

                    attempts -= 1                                                                   # Removing one attempt after each guess until it reaches zero
                    print("Attempts left:", attempts)                                               # Reminder of how many attempts are left 

                if attempts == 0:                                                                   # Checking how many attempts are left since while loop is not running anymore
                    print("Game Over! The number was:", secret)                                     # Giving a end of the game notification
                    rounds_played += 1                                                              # Adding one to the rounds played
                    print("Rounds played:", rounds_played)                                          # Notification for the player
                    attempts = 5                                                                    # Resetting the attempts

            if rounds_played == total_rounds:                                                       # checking if all srounds were played
                print(f"You won {rounds_won} round(s) out of {rounds_played}")                      # End result