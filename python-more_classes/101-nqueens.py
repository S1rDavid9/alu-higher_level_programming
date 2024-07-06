#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check if there's a queen in the same column up to the current row
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row, N, solutions):
    """
    Recursive function to solve N queens problem using backtracking.
    """
    if row == N:
        # Found a solution, convert board to required format and store it
        solutions.append(board[:])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place queen
            board[row] = col

            # Recur to place rest of the queens
            solve_nqueens(board, row + 1, N, solutions)

            # Backtrack: remove queen and try other positions
            board[row] = -1

def nqueens(N):
    """
    Solve the N queens problem and print all solutions.
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize empty board representation (array of size N with -1 indicating no queen)
    board = [-1] * N
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    # Print all solutions
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
