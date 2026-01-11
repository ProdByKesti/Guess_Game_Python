import random

# Giving hints if the guess was wrong
def give_hints(secret, guess):
    if secret % 2 == 0:                                                                             
        print("The number we are looking for is even")
    else:                                                                                           
        print("The number we are looking for is odd")
    
    distance = abs(secret - guess)                                                                  
    if distance <= 2:                                                                                                                                     
        print("Hot")
    elif distance <= 5:
        print("Warm")
    else:
        print("Cold")

    if guess < secret:                                                                              
        print("Too low")
    elif guess > secret:
        print("Too high")

# Playing a round in arcade mode
def play_round(min_num, max_num, max_attempts):
    secret = random.randint(min_num, max_num)                                                       
    attempts = max_attempts                                                                        

    while attempts > 0:                                                                             
        guess_input = input(f"Guess a Number ({min_num}-{max_num}): ")                              

        if not guess_input.isdigit():                                                               
            print("Please enter a valid number.")
            continue                                                                                

        guess = int(guess_input)                                                                   

        if guess < min_num or guess > max_num:                                                     
            print(f"Number must be between {min_num} and {max_num}.")                         
            continue                                                                                

        if guess == secret:                                                                         
            print("You win!")                                                                       
            return True                                                                            
        print("Wrong guess!")                                                                       
        give_hints(secret, guess)                                                                

        attempts -= 1                                                                              
        print(f"Attempts left: {attempts}")                                                         

    print(f"You lost! The number was {secret}")                                                    
    return False 
                                                                                  
# Playing a round in adventure mode
def play_chest(min_num, max_num, attempts, inventory, health):
    secret = random.randint(min_num, max_num)                                                       

    while attempts > 0:                                                                             
        print("\n[g] Guess the number")
        print("\n[i] Use item")

        action = input("Choose action:").strip().lower()

        if action == "i":
            health = use_item_menu(inventory, health, secret, min_num, max_num)
            continue

        if action != "g":
            print("Invalid choice.")
            continue

        guess_input = input(f"Guess a Number ({min_num}-{max_num}): ").strip()                              

        if not guess_input.isdigit():                                                                
            print("Please enter a valid number.")
            continue                                                                                 

        guess = int(guess_input)                                                                    

        if guess < min_num or guess > max_num:                                                      
            print(f"Number must be between {min_num} and {max_num}.")                               
            continue                                                                                

        if guess == secret:                                                                         
            print("The chest unlocks!")                                                                       
            return True                                                                             
        
        print("Wrong guess!")                                                                       
        give_hints(secret, guess)                                                                   

        attempts -= 1                                                                               
        print(f"Attempts left: {attempts}")                                                         

    print(f"The chest remains sealed! The number was {secret}")                                                     
    return False  
 
# Choosing difficulty in arcade mode
def choose_difficulty():
    while True:                                                                                     
        choice = input("Choose difficulty (easy/medium/hard)").lower()                              

        if choice == "easy":                                                                    
            return 1, 10, 5                                                                         
        elif choice == "medium":
            return 1, 20, 4
        elif choice == "hard":
            return 1, 50, 3
        else:
            print("Invalid difficulty.") 

# Showing the intro story text in adventure mode
def print_intro_story():
    print("""
          You are a treasure hunter exploring ancient ruins.
          Deep underground, magical chests block your path.
          Each chest is sealed with a mysterious number lock.
          
          Unlock the chests to survive.
          Fail - and the ruins will claim you.
          """)
    
# Setting different difficulty for each round in the adventure mode
def scale_difficulty(round_number):
    min_num = 1
    max_num = 10 + round_number * 5
    attempts = max(3, 6 - round_number // 2)
    return min_num, max_num, attempts

# A list of stories for every chest in adventure mode
CHEST_STORIES = ["You enter a damp stone chamber. Moss covers the walls.",
                 "A narrow hallway opens into a torch-lit room.",
                 "The air grows cold as you step into a forgotten vault.",
                 "You hear chains rattling as you approach the next chamber.",
                 "Ancient carvings glow faintly around the sealed chest.",
                 "Dust fills the air as a heavy stone door closes behind you.",
                 "The ground trembles. Something doesnt want you here.",
                 "A golden light leaks through cracks in the chest.",
                 "The silence here feels unnatural.",
                 "You reach the heart of the ruins. This chest feels different."]

# The command to print the right chest story for every round in adventure mode
def print_chest_story(round_number):
    index = min(round_number - 1, len(CHEST_STORIES) - 1)
    print("\n" + CHEST_STORIES[index])
    print(f"A mysterious chest blocks your path (Chest {round_number}).")

# The player can choose how many rounds they want to play in arcade mode
def choose_rounds():
    total_rounds = 0                                                                                   

    while total_rounds < 1:                                                                             
                                                                                 
        user_input1 = input("How many rounds do you want to play?: ")                                   

        if not user_input1.strip().isdigit():                                                           
            print("Please enter a valid number")                                                        
            continue                                                                                   

        total_rounds = int(user_input1)                                                                 
        return total_rounds
    
# The Loop for playing a game in arcade mode
def arcade_mode():
    min_num, max_num, attempts = choose_difficulty()                                                    
    total_rounds = choose_rounds()
    wins = 0                                                                                            

    for round_number in range(1, total_rounds + 1):                                                     
        print(f"\n---Round {round_number}---")                                                          
        if play_round(min_num, max_num, attempts):                                                     
            wins +=1                                                                                  

    print(f"\nGame over! You won {wins} out of {total_rounds} Rounds.")

# There is a chance to drop one or two items after each round
def roll_item_drop(inventory):
    roll = random.random()

    if roll < 0.15:
        inventory["diamond"] += 1
        print("You found a diamond!")

    elif roll < 0.35:
        inventory["health_potion"] += 1
        print("You found a health potion!")
        
# Showing the player life and inventory
def print_player_status(health, inventory):
    print(f"\nHealth: {health}")
    print(f"Diamonds: {inventory['diamond']}")
    print(f"Health Potions: {inventory['health_potion']}")

# Using a diamond will tell you if the secret number is in the upper or lower half of the range
def use_diamond(secret, min_num, max_num):
    midpoint = (min_num + max_num) // 2
    print("Super Hint Activated!")

    if secret > midpoint:
        print("The number is in the UPPER half of the range.")
    else:
        print("The number is in the LOWER half of the range.")

# Using a health potion will add 25 health to the players health, Max health is limited to 100
def use_health_potion(health):
    heal = 25
    print(f"You drink a health potion and restore {heal} HP.")
    health = min(health + heal, 100)
    return health

# The menu for using items, It wil also tell the player if they have no items to use
def use_item_menu(inventory, health, secret, min_num, max_num):
    while True:
        print("\nInventory")
        print(f"Diamonds: {inventory['diamond']}")
        print(f"Health Potions: {inventory['health_potion']}")
        print("[d] Use diamond (super hint)")
        print("[h] Use health potion (25 health)")
        print("[b] Back")

        choice = input("Choose an item: ").strip().lower()

        if choice == "d":
            if inventory["diamond"] > 0:
                inventory["diamond"] -= 1
                use_diamond(secret, min_num, max_num)
                return health
            else:
                print("You have no diamonds.")
        
        elif choice == "h":
            if inventory["health_potion"] > 0:
                inventory["health_potion"] -= 1
                health = use_health_potion(health)
                return health
            else:
                print("You have no health potions.")
        
        elif choice == "b":
            return health
        
        else:
            print("Invalid choice.")

# The Loop for playing a game in adventure mode
def adventure_mode():
        
    health = 100
    inventory: dict[str, int] = {"diamond": 0, "health_potion": 1}

    print_intro_story()

    for round_number in range(1,11):
        print_chest_story(round_number)

        min_num, max_num, attempts = scale_difficulty(round_number)

        won = play_chest(min_num, max_num, attempts, inventory, health)

        if not won:
            health -= 20
            print("A trap is triggered! You loose 20 health")

        if health <= 0:
            print("Your adventure ends here...")
            return
        
        if won:
            roll_item_drop(inventory)
        print_player_status(health, inventory)

    print("\nYou escaped the ruins with legendary treasure!")

# The main menu 
while True:

    choose_mode = input("Choose a mode arcade/adventure:").lower()

    if choose_mode == "arcade":
        arcade_mode()
        break
    elif choose_mode == "adventure":
        adventure_mode()
        break
    else:
        continue



