N = 8  # Size of the chessboard

def solveNQueens(board, col):
    # Base case: If all queens are placed
    if col == N:
        for row in board:
            print(row)
        print()
        return True

    # Try placing the queen in each row of the current column
    for i in range(N):
        if isSafe(board, i, col):
            # Place queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solveNQueens(board, col + 1):
                return True

            # Backtrack if placing queen at (i, col) doesn't lead to a solution
            board[i][col] = 0

    return False  # No place for queen in this column

def isSafe(board, row, col):
    # Check the row to the left
    for x in range(col):
        if board[row][x] == 1:
            return False

    # Check the upper diagonal on the left
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    # Check the lower diagonal on the left
    for x, y in zip(range(row, N), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True

# Initialize the chessboard
board = [[0 for x in range(N)] for y in range(N)]

# Start the algorithm
if not solveNQueens(board, 0):
    print("No solution found")
