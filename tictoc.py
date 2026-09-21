import random

board = [" " for i in range(9)]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner():
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in lines:
        a, b, c = line
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


print("TIC TAC TOE")
print("You = X")
print("Computer = O")

while True:
    show_board()

    # Player move
    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] != " ":
        print("Position already taken!")
        continue

    board[pos] = "X"

    if winner() == "X":
        show_board()
        print("You win!")
        break

    if " " not in board:
        show_board()
        print("Draw!")
        break

    # Computer move
    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    computer = random.choice(empty)
    board[computer] = "O"

    if winner() == "O":
        show_board()
        print("Computer wins!")
        break

    if " " not in board:
        show_board()
        print("Draw!")
        break
