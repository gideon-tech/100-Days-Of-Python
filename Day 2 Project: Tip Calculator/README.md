# Day 2: Tip Calculator 💰

## Project Description

A simple command-line tip calculator that helps split bills among multiple people, including a customizable tip percentage.

## What I Learned

- Working with `float()` and `int()` for user input conversion
- Performing percentage calculations in Python
- Using the `round()` function for decimal precision
- String formatting with f-strings

## How to Run

```bash
python main.py
```

## Usage Example

```
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10 12 15 15
How many people to split the bill? 5
Each person should pay: $34.5
```

## Features

- Calculate tips based on custom percentages (10%, 12%, 15%, or any custom amount)
- Split bills evenly among any number of people
- Round to 2 decimal places for accurate money amounts

## Challenges Faced

- Understanding the difference between integer division and float division
- Ensuring proper rounding for monetary values

## Code Highlights

```python
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
final_amount = round(bill_per_person, 2)
```

---

**Day:** 2/100  
**Date:** October 9, 2025  
**Topics:** Basic Math Operations, User Input, Data Types
