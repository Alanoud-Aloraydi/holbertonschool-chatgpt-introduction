#!/usr/bin/python3
"""
Tic Tac Toe game.
Features robust input validation, accurate win detection, and tie-game logic.
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Checks if the board has no empty spaces left."""
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """Helper function to ensure user inputs are valid integers: 0, 1, or 2."""
    while True:
        try:
            val = int(input(prompt))
            if val in [0, 1, 2]:
                return val
            else:
                print("Error: Invalid position. Please enter 0, 1, or 2.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        row = get_valid_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = get_valid_input("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] == " ":
            # 1. Place the piece
            board[row][col] = player
            
            # 2. Check for win BEFORE switching players
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
                
            # 3. Check for tie
            if is_board_full(board):
                print_board(board)
                print("The game is a tie!")
                break
                
            # 4. Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
