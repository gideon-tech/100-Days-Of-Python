# Day 6: Maze 🧩

## Project Description

A maze-solving algorithm built using Reeborg's World. The robot navigates through a maze by following the right-hand rule - it always tries to turn right first, then move forward, or turn left if necessary until it reaches the goal.

## What I Learned

- Creating custom functions in Python
- Working with while loops and conditions
- Implementing the right-hand rule algorithm
- Using logical operators (and, or, not)
- Understanding nested conditionals (if, elif, else)
- Problem-solving with algorithms

## How to Run

This project is designed to run on [Reeborg's World](https://reeborg.ca/reeborg.html):

1. Visit https://reeborg.ca/reeborg.html
2. Select a maze challenge (e.g., "Maze" or "Hurdles")
3. Copy and paste the code from `main.py`
4. Click "Run" to watch the robot solve the maze

## Algorithm Explanation

The code uses the **right-hand rule** to solve the maze:

1. If the right side is clear → turn right and move
2. Else if the front is clear → move forward
3. Else → turn left

This continues until the robot reaches the goal.

## Features

- Custom `turn_right()` function (since Reeborg only has `turn_left()`)
- Automated maze solving using conditional logic
- Works with various maze configurations in Reeborg's World

## Challenges Faced

- Understanding the right-hand rule algorithm
- Creating a turn_right() function using only turn_left()
- Determining the correct order of conditional checks

## Code Highlights

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
```

## Reeborg's World Functions Used

- `turn_left()` - Built-in function to turn left
- `move()` - Move forward one step
- `at_goal()` - Check if robot reached the goal
- `right_is_clear()` - Check if right side is clear
- `front_is_clear()` - Check if front is clear

---

**Day:** 6/100  
**Date:** January 8, 2026  
**Topics:** Functions, While Loops, Conditional Logic, Algorithms