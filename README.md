# 🎲 Number Guessing Game (Python)

A console-based number guessing game written in Python.  
This project started as a simple guessing game and was gradually expanded with *difficulty levels, refactored code structure, and an advanced hint system*.

It’s designed as a learning project to practice *core Python concepts* in a practical and fun way.

---

## 🚀 Features

- Random secret number generation
- Multiple difficulty levels
- Customizable number of attempts
- Multiple rounds per game
- Input validation (only valid integers allowed)
- *Advanced hint system*
  - Even / Odd hint
  - Cold / Warm / Hot distance-based hints
- Clean and readable code using *functions*
- No duplicated logic (refactored)

---

## 🕹 How to Play

1. Start the game
2. Choose a difficulty (easy, medium, hard)
3. Choose how many rounds you want to play
4. Guess the secret number within the allowed attempts
5. Use hints to narrow down the correct number
6. Try to win as many rounds as possible

---

## 🎚 Difficulty Levels

| Difficulty | Number Range | Attempts |
|----------|--------------|----------|
| Easy     | 1 – 10       | 5 attempts |
| Medium   | 1 – 20       | 4 attempts |
| Hard     | 1 – 50       | 3 attempts |

---

## 💡 Hint System

After an incorrect guess, the game provides helpful hints:

- *Even / Odd*  
  Indicates whether the secret number is even or odd

- *Cold / Warm / Hot*
  - 🔥 Hot: very close to the secret number
  - 🌡 Warm: somewhat close
  - ❄ Cold: far away from the secret number

This makes the game more interactive and strategic.

---

## 🧠 Code Structure

The code is organized using functions to avoid repetition and improve readability:

- choose_difficulty() – handles difficulty selection
- play_round() – runs one full round of the game
- give_hints() – handles all hint logic
- Additional helper functions for validation and game flow

This structure makes the project easier to extend and maintain.

---

## 🧩 What I Learned

- Using functions to remove duplicated code
- Passing parameters and using return values
- Input validation and error handling
- Game loop logic
- Basic game design and user feedback
- Refactoring existing code into cleaner solutions

---

## 🛠 Technologies Used

- Python 3
- Standard library only (random)

---

## 📦 Future Ideas

- Add achievements
- Add score tracking
- Difficulty-based hint limitations
- Timer-based mode
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
Make sure Python 3 is installed, then run:

```bash
python guessing_game.py
