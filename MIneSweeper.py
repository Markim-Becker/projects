import random

# Constants for the game
MINE = "*"
EMPTY = " "
SIZE = 8
MINES = 10

# Initialize the board
board = [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

# Place mines randomly on the board
mines_placed = 0
while mines_placed < MINES:
    row = random.randint(0, SIZE - 1)
    col = random.randint(0, SIZE - 1)
    if board[row][col] != MINE:
        board[row][col] = MINE
        mines_placed += 1

# Function to count the number of adjacent mines for a given square
def count_adjacent_mines(row, col):
    count = 0
    for r in range(max(0, row - 1), min(row + 2, SIZE)):
        for c in range(max(0, col - 1), min(col + 2, SIZE)):
            if board[r][c] == MINE:
                count += 1
    return count

# Main game loop
game_over = False
while not game_over:
    # Print the current state of the board
    for row in board:
        print(" ".join(row))
    print()

    # Get a guess from the player
    row = int(input("Guess row (0-7): "))
    col = int(input("Guess col (0-7): "))

    # Check if the guess is a mine
    if board[row][col] == MINE:
        print("Sorry, you hit a mine! Game over.")
        game_over = True
    else:
        # Count the number of adjacent mines
        count = count_adjacent_mines(row, col)
        board[row][col] = str(count)

        # Check if the player has won
        if sum(row.count(EMPTY) for row in board) == MINES:
            print("Congratulations, you've cleared all the mines and won the game!")
            game_over = True

# Print the final state of the board
for row in board:
    print(" ".join(row))

