"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = sum(i.count(X) for i in board)
    oCount = sum(i.count(O) for i in board)

    if xCount == 0 or xCount == oCount:
        return X
    elif xCount > oCount:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                options.add((i, j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copied_board = copy.deepcopy(board)
    try:
        i, j = action
        copied_board[i][j] = player(copied_board)
    except Exception:
        print("Error")
    return copied_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xCount = 0
    oCount = 0
    # lines
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
        # counters
        if xCount == 3:
            return X
        elif oCount == 3:
            return O
        else:
            xCount = 0
            oCount = 0

    # columns
    for i in range(3):
        for j in range(3):
            if board[j][i] == X:
                xCount += 1
            elif board[j][i] == O:
                oCount += 1
        # counters
        if xCount == 3:
            return X
        elif oCount == 3:
            return O
        else:
            xCount = 0
            oCount = 0
    # Main diagonal
    for i in range(3):
        for j in range(3):
            if i == j:
                if board[i][j] == O:
                    oCount += 1
                elif board[i][j] == X:
                    xCount += 1
    # counters
    if xCount == 3:
        return X
    elif oCount == 3:
        return O
    else:
        xCount = 0
        oCount = 0
    # secondary diagonal
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                if board[i][j] == O:
                    oCount += 1
                elif board[i][j] == X:
                    xCount += 1
    # counters
    if xCount == 3:
        return X
    elif oCount == 3:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win == X or win == O or len(actions(board)) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        print(f"A in min: {action[0]}, {action[1]}")
        value = min(v, max_value(result(board, action)))
        print(f"V in min: {value}")
        if value < v:
            v = value
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        print(f"A in max: {action[0]}, {action[1]}")
        value = max(v, min_value(result(board, action)))
        print(f"V in max: {value}")
        if value > v:
            v = value
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    if player(board) == X:
        return min_value(board)
    else:
        return min_value(board)