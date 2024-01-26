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
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    # columns
    for i in range(3):
        if board[0][i] == X and board[1][i] == X and board[2][i] == X:
            return X
        elif board[0][i] == O and board[1][i] == O and board[2][i] == O:
            return O

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
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            score = min_value(result(board, action))
            if score > v:
                v = score
                ac = action
    else:
        v = math.inf
        for action in actions(board):
            score = max_value(result(board, action))
            if score < v:
                v = score
                ac = action
    return ac