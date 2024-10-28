
# Tic Tac Toe

This project is a Tic-Tac-Toe game with a graphical user interface, built using Python and `tkinter`. It offers a simple, intuitive interface for two players who take turns selecting boxes on a 3x3 grid. The game recognizes the winner, detects a draw, and provides an option to restart.

## Features

- **Player Switching**: The game automatically switches between Player X and Player O.
- **Winner Detection**: As soon as a player completes a horizontal, vertical, or diagonal line, they are announced as the winner.
- **Draw Detection**: Recognizes a draw when the entire grid is filled and no player has won.
- **Restart Option**: A restart button is available to start a new game round without restarting the program.
- **Winner Display**: Displays the winning player after each round.

## Installation

1. Make sure Python 3 is installed.
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe

Install tkinter if not already installed (it is often pre-installed):

For Ubuntu/Debian: sudo apt-get install python3-tk

Run the game: python3 tic_tac_toe.py


## How to play
1. Starting the Game: When launched, a window with a 3x3 grid appears.
2. Player Moves: Player X begins and clicks on a free cell. The player alternates after each turn.
3. Winner Announcement: As soon as a player aligns three cells in a row (horizontally, vertically, or diagonally), they are announced as the winner.
4. Draw Detection: If all cells are occupied but no player has won, a draw message is displayed.
5. Restart: Click the restart button to begin a new round.
