def print_board(board):
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} ", end="|")
        print("\n-------------")

def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != "-":
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([row[col] for row in board])) == 1 and board[0][col] != "-":
            return board[0][col]

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] or
            board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "-":
        return board[1][1]

    return None

def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None

    print("Welcome to Tic-Tac-Toe!")
    print("Player X goes first. Enter row and column numbers to make your move.")

    while not winner:
        print_board(board)

        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter the row number (0-2): "))
                col = int(input("Enter the column number (0-2): "))

                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "-":
                    board[row][col] = current_player
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        winner = check_winner(board)

        if not winner:
            current_player = "O" if current_player == "X" else "X"

    print_board(board)
    print(f"Player {winner} wins!")

tic_tac_toe()
