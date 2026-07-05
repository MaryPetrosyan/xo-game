# Tic-Tac-Toe Game (OOP Python)

## Description

This project is a simple implementation of the classic **Tic-Tac-Toe** game using **Object-Oriented Programming (OOP)** principles in Python.

The game consists of two main classes:

* **Board** – Manages the game board, player moves, and game state.
* **Player** – Represents a player and their mark (`X` or `O`).

The board size is configurable, allowing games larger than the standard 3×3 grid.

## Features

* Create an `m × m` game board.
* Display the current board state.
* Validate player moves.
* Detect winning rows.
* Detect winning columns.
* Detect winning diagonals.
* Detect draw situations.
* Support multiple board sizes.
* Clean OOP-based design.

## Project Structure

```text
Board
 ├── display_board()
 ├── move()
 └── check_winner()

Player
 └── move()
```

## How It Works

1. A board is created with a specified size.
2. Players are assigned marks (`X` and `O`).
3. Players make moves by selecting row and column positions.
4. The board validates each move.
5. After every move, the game checks:

   * Rows
   * Columns
   * Main diagonal
   * Anti-diagonal
6. The game returns one of the following states:

   * `WINNER X`
   * `WINNER O`
   * `CONTINUE`
   * `DRAW`

## Example

```python
board = Board(3)

p1 = Player("Player 1", "X")
p2 = Player("Player 2", "O")

p1.move(board, 0, 0)
p2.move(board, 1, 1)
p1.move(board, 0, 1)
p1.move(board, 0, 2)

print(board.display_board())
print(board.check_winner())
```

## Sample Output

```text
 X  X  X
 .  O  .
 .  .  .

WINNER X
```

## Requirements

* Python 3.8+

## Run

```bash
python main.py
```

## Concepts Used

* Classes and Objects
* Encapsulation
* Object-Oriented Programming (OOP)
* Lists and List Comprehensions
* Game Logic Validation



Mery Petrosyan

