# 🗝 Treasure Chest Guessing Game (Python)

A text-based Python game that combines a classic number guessing mechanic with *arcade gameplay, **adventure progression, **items, and **story elements*.  

This project is designed as a learning journey into Python fundamentals such as *functions, loops, conditionals, and game state management*, while providing a fun and interactive experience.

---

## 🚀 Features

- Random secret number generation
- Multiple difficulty levels
- Customizable number of attempts
- Multiple rounds per game
- Input validation (only valid integers allowed)
- *Advanced hint system*
  - Higher / Lower hints
  - Even / Odd hints
  - Cold / Warm / Hot distance-based hints
- *Arcade and Adventure modes*
  - Arcade: independent rounds with scoring
  - Adventure: story-driven treasure hunt with health and items
- *Items system*
  - Diamonds (super hints)
  - Health potions
- Player health management (Adventure mode)
- Clean and readable code using *functions*
- No duplicated logic (refactored)

---

## 🕹 How to Play

1. Start the game  
2. Choose a game mode (arcade or adventure)  
3. If Arcade Mode:  
   - Choose difficulty (easy / medium / hard)  
   - Choose number of rounds  
4. If Adventure Mode:  
   - Progress through chests with a limited health pool  
   - Health decreases when you lose a chest  
   - Winning chests may drop items  
5. Guess the secret number within the allowed attempts  
6. Use hints and items strategically  
7. Try to complete as many rounds or chests as possible

---

## 🎚 Difficulty Levels

| Difficulty | Number Range | Attempts |
|------------|--------------|----------|
| Easy       | 1 – 10       | More attempts |
| Medium     | 1 – 20       | Fewer attempts |
| Hard       | 1 – 50       | Limited attempts |

Adventure Mode scales difficulty automatically as you progress.

---

## 💡 Hint System

After an incorrect guess, the game provides helpful hints:

- *Higher / Lower* – whether the guess is too low or too high  
- *Even / Odd* – whether the secret number is even or odd  
- *Cold / Warm / Hot* – based on distance from the secret number  
  - 🔥 Hot: very close  
  - 🌡 Warm: somewhat close  
  - ❄ Cold: far away  

---

## 🎒 Items System (Adventure Mode)

Items can drop randomly after winning a chest:

### 💎 Diamond (Super Hint)
- Rare drop  
- Reveals powerful hints about the secret number  
- Can be used anytime during a round

### 🧪 Health Potion
- Restores player health  
- Essential for survival in Adventure Mode

Items are managed through an interactive inventory menu.

---

## ❤ Health System (Adventure Mode)

- Player starts with a fixed amount of health  
- Losing a chest reduces health  
- Health potions restore health  
- Game over when health reaches 0

---

## 🧩 Code Structure

The project uses functions heavily for modularity and clarity:

- choose_difficulty() — handles difficulty selection  
- play_round() — runs one round of the game (basic guessing logic)  
- give_hints() — handles all hint logic  
- arcade_mode() — manages arcade-style gameplay  
- adventure_mode() — manages story progression, health, and items  
- scale_difficulty() — increases difficulty dynamically in Adventure Mode  
- play_chest() — core guessing logic for Adventure Mode  
- use_item_menu() — allows player to use items during a round  
- roll_item_drop() — handles random item rewards  
- print_player_status() — displays health and inventory  
- print_intro_story() — shows the game narrative  
- Additional helper functions for input validation, game flow, and scoring

This structure keeps the code clean, reusable, and easy to extend.

---

## 🧠 What I Learned

- Using functions to remove duplicated code  
- Passing parameters and using return values  
- Input validation and error handling  
- Game loop logic and score tracking  
- Basic game design, story progression, and player feedback  
- Modular code design for scalability  
- Managing game state (health, items, difficulty)  

---

## 🛠 Technologies Used

- Python 3  
- Standard library only (random)  

---

## 📦 Future Ideas

- Add achievements and unlockables  
- Expand item types and effects  
- Timer-based rounds or challenges  
- GUI version  

---

## 📄 Version History

### v1.0.0
- Basic number guessing game  

### v1.1.0
- Added difficulty levels  
- Added attempt limits  

### v1.2.0
- Refactored duplicated code into functions  
- Improved code readability and structure  

### v1.3.0
- Added advanced hint system:
  - Even / Odd hints  
  - Cold / Warm / Hot distance hints  

### v2.0.0
- Renamed to Treasure Chest Guessing Game  
- Added *Arcade and Adventure modes*  
- Added *story and narrative progression*  
- Added *health system* (Adventure Mode)  
- Added *items system* (Diamonds, Health Potions)  
- Dynamic difficulty scaling in Adventure Mode  
- New functions:
  - arcade_mode()  
  - adventure_mode()  
  - scale_difficulty()  
  - play_chest()  
  - use_item_menu()  
  - roll_item_drop()  
  - print_player_status()  
  - print_intro_story()
