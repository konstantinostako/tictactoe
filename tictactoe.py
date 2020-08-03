"""
Tic Tac Toe Player
"""

import math
import copy

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
    if board == initial_state:
        player = X
        return X
    
    counter_X = 0
    counter_O = 0
    for items in board:
        counter_X += items.count(X)
        counter_O += items.count(O)
    
    if counter_X == counter_O:
        player = X
        return player
    else:
        player = O
        return player
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                moves.append([row, column])

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == None:
        print("Error")
        return board
    else:
        newBoard = copy.deepcopy(board)
        try:
            if newBoard[action[0]][action[1]] != EMPTY:
                raise IndexError
            else:
                newBoard[action[0]][action[1]] = player(newBoard)
                return newBoard
        except IndexError:
            print("Move is not allowed")



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if board[row][0] == X and board[row][1] == X and board[row][2] == X:
            return X
        if board[row][0] == O and board[row][1] == O and board[row][2] == O:
            return O
    
    for column in range(3):
        if board[0][column] == X and board[1][column] == X and board[2][column] == X:
            return X
        if board[0][column] == O and board[1][column] == O and board[2][column] == O:
            return O

    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    return None

    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    
    for row in range(3):
        for column in range(3):
            if (board[row][column] == EMPTY):
                return False
    
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if (terminal(board)):
        if (winner(board) == X):
            return 1
        if (winner(board) == O):
            return -1
        else:
            return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Find the current player
    currentPlayer = player(board)

    if currentPlayer == X: # Need to maximize result
        print("Entered CurrentPlayer: X")
        v = -math.inf
        for action in actions(board):
            newResult = minValue(result(board, action))
            print(newResult)
            if newResult > v:
                v = newResult
                optimalMove = action
    else: # Need to minimize result
        print("Entered CurrentPlayer: O")
        v = math.inf
        for action in actions(board):
            newResult = maxValue(result(board, action))
            if newResult < v:
                v = newResult
                optimalMove = action
    print(optimalMove)
    return optimalMove

def maxValue(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minValue(result(board, action)))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))
    return v
