# 🎲 Number Guessing Game (Python)

A beginner-friendly number guessing game written in Python.  
The player must guess a randomly generated number within a limited number of attempts.

This project is part of my Python learning journey and focuses on clean logic, input validation, and game design using loops and conditionals.

---

## 🚀 Features

- Random secret number generated every round
- Input validation (only integers allowed)
- Enforced number ranges based on difficulty
- Limited attempts per round
- Multi-round gameplay
- Player chooses how many rounds to play
- Score tracking across rounds
- Clear feedback after each guess (Too high, Too low, You win, Game over)

---

## 🎚 Difficulty Levels

The player can choose between three difficulty modes:

| Difficulty | Number Range | Attempts |
|-----------|--------------|----------|
| Easy      | 1 – 10       | 3        |
| Medium    | 1 – 20       | 4        |
| Hard      | 1 – 50       | 5        |

Each round uses the selected difficulty settings.

---

## 🕹 How the Game Works

1. The player selects a difficulty level.
2. The player chooses how many rounds they want to play.
3. For each round:
   - A random number is generated based on the difficulty.
   - The player has a limited number of attempts to guess the number.
   - Feedback is given after each guess.
4. The game tracks how many rounds the player wins.
5. At the end, the final score is displayed.

---

## 🧠 What I Learned

- Using while loops for game flow
- Nested loops (round loop + guessing loop)
- Input validation with .isdigit()
- Safe type conversion using int()
- Generating random numbers with random.randint()
- Using break and continue correctly
- Structuring code for readability and maintainability

---

## ▶ How to Run the Game

Make sure Python 3 is installed, then run:

```bash
python guessing_game.py
