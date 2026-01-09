# 🎲 Number Guessing Game (Python)

A simple, beginner-friendly number guessing game written in Python.  
The player tries to guess a randomly generated number within a limited number of attempts.

This project is part of my Python learning journey and focuses on clean logic, input validation, and game loops.

---

## 🚀 Features

- Random secret number every round
- Input validation (only numbers allowed)
- Number range enforcement (e.g. 1–10)
- Multiple attempts per round
- *NEW:* Multi-round gameplay
- *NEW:* Player chooses how many rounds to play
- *NEW:* Score tracking across rounds
- Clear feedback (Too high, Too low, You win, Game over)

---

## 🕹 How the Game Works

1. The player chooses how many rounds they want to play.
2. For each round:
   - A random number between 1 and 10 is generated.
   - The player has a limited number of attempts to guess it.
   - Feedback is given after each guess.
3. The game tracks how many rounds the player wins.
4. At the end, the final score is displayed.

---

## 🧠 What I Learned

- Using while loops for game flow
- Nested loops (round loop + guessing loop)
- Input validation with .isdigit()
- Converting user input safely with int()
- Using random.randint()
- Using break and continue correctly
- Writing clean, readable Python code

---

## ▶ How to Run the Game

Make sure Python 3 is installed, then run:

```bash
python guess_game.py
