# Hand Cricket Game

A simple command-line Hand Cricket game built using Python.  
This game is inspired by the classic hand cricket game played between friends.

The player competes against the computer in a toss-based cricket match where batting and bowling are decided after the toss.

---

# Game Rules

## Toss
- Choose:
  - `0 = Heads`
  - `1 = Tails`
- The computer randomly performs the toss.
- Winner of the toss chooses:
  - Batting
  - Bowling

---

## Batting & Bowling
- Both batsman and bowler choose a number from **1 to 10** simultaneously.
- If both numbers match:
  - The batsman is **OUT**
- If numbers do not match:
  - The batsman’s chosen number is added to the score.
- After getting out:
  - Roles switch between batting and bowling.
- The player with the higher score wins the match.

---

# Features

- Toss system
- Batting and bowling selection
- Randomized computer gameplay
- Score tracking
- Win/Lose/Draw result system
- Two innings gameplay
- Command-line based game

---

# Technologies Used

- Python
- `random` module
- `time` module

---

# How to Run the Game

## 1. Clone the Repository

```bash
https://github.com/KRISHNA-VALLABHANENI/Hand_Cricket/tree/main
```

## 2. Navigate to the Project Folder

```bash
cd Hand_Cricket
```

## 3. Run the Python File

```bash
python hand_cricket.py
```

---

# Sample Gameplay

```text
0 = Heads
1 = Tails
Heads or Tails: 0

Computer is Tails
You are Heads
Toss is Heads

--you won the toss--

0 > Batting
1 > Bowling: 0

You choose Batting

PLAYER: 5
Comp = 3

PLAYER: 7
Comp = 7

No.of balls = 2
your'e score = 5
```

---

# Screenshots
<img width="375" height="526" alt="image" src="https://github.com/user-attachments/assets/2e67f11a-beef-4ab9-be91-eab6170b9f5d" />

# What I Learned

While building this project, I practiced:

- Python basics
- Functions
- Conditional statements
- Loops
- Random number generation
- Game logic implementation
- User input handling

---

# Future Improvements

- Multiplayer mode
- GUI version using Tkinter or Pygame
- Better scorecard display
- Difficulty levels
- Match statistics
- Input validation improvements
