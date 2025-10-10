# Day 3: Treasure Island Game 🏝️

## Project Description

An interactive text-based adventure game where players navigate through a series of choices to find hidden treasure. Players must make the right decisions at each crossroad, lake, and mysterious house to win the game. Wrong choices lead to game over scenarios!

## What I Learned

- Working with conditional statements (`if`, `elif`, `else`)
- Implementing nested conditional logic for complex decision trees
- Using the `.lower()` method for case-insensitive input handling
- Creating an interactive command-line game with multiple branching paths
- Using multi-line strings with raw string literals (`r'''`) for ASCII art

## How to Run

```bash
python main.py
```

## Usage Example

```
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go?Type "left" or "right"
left
You've come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across.
wait
You arrive at the island unharmed. There is a house with 3 doors.One "red", one "yellow" and one "blue".Which color do you choose?
yellow
You found the treasure! You win
```

## Features

- ASCII art treasure island display at the start
- Multiple decision points creating different story paths
- Case-insensitive input handling for better user experience
- Five different possible endings:
  - **Win**: Choose left → wait → yellow door
  - **Game Over 1**: Choose right (fall into a hole)
  - **Game Over 2**: Choose left → swim (attacked by animal)
  - **Game Over 3**: Choose left → wait → red door (burned by fire)
  - **Game Over 4**: Choose left → wait → blue door (eaten by beasts)
  - **Game Over 5**: Choose left → wait → invalid door choice

## Challenges Faced

- Structuring nested if-elif-else statements correctly for multiple branching paths
- Ensuring proper indentation for nested conditional blocks
- Handling all possible user input combinations
- Creating a logical flow that makes sense for the story

## Code Highlights

```python
# Nested conditional logic for complex decision tree
if choice1 == "left":
    choice2 = input('You\'ve come to a lake...')
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed...')
        if choice3 == "yellow":
            print("You found the treasure! You win")

# Case-insensitive input handling
choice1 = input('Type "left" or "right"\n').lower()
```

---

**Day:** 3/100  
**Date:** October 10, 2025  
**Topics:** If statements, Nested If Statements, Multiple Ifs, Logical Operations
