import tictactoe as ttt

# Python3 code to demonstrate
# Search None in Matrix
X = "X"
O = "O"
EMPTY = None


# initializing list
matrix = [[O, X, X],
            [X, EMPTY, O],
            [X, O, X]]


print(ttt.terminal(matrix))
print(ttt.result(matrix, (2, 2)))
print(ttt.winner(matrix))