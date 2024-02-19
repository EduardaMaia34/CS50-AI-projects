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
    - always startes with X
    """
    emp = 0


    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                emp += 1
        
    if (emp%2):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board
    """
    #see if the action is a valid action
    if action not in actions(board):
        raise Exception("Not valid action")

    #add action to the board without modifying it
    i,j = action
    board_copy = copy.deepcopy(board)
    #add the action (put X or O) based on the player's turn
    board_copy[i][j] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0]==X:
                    return X
                elif board[i][0]==O:
                    return O
            elif board[0][j] == board[1][j] == board[2][j]:
                if board[0][j]==X:
                    return X
                elif board[0][j]==O:
                    return O
            elif board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
                if board[1][1]==X:
                    return X
                elif board[1][1]==O:
                    return O
            else:
                return None #no winner (yet)
    
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                return False
    return True #tie



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0
                


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): #game over
        return None
    
    elif player(board)==X:
        plays=[]

        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    elif player(board)==O:
        plays=[]

        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]


def max_value(board):
    v = -math.inf
    if terminal(board): #game over?
        return utility(board) #if yes, than who won
    for action in actions(board):
        v = max(v, min_value(result(board, action))) 
        #its gonna choose the maximum value we can get with the possible actions
    return v


def min_value(board):
    v = math.inf
    if terminal(board): #game over?
        return utility(board) #if yes, than who won
    for action in actions(board):
        v = min(v, max_value(result(board, action))) 
        #its gonna choose the minimum value we can get with the possible actions
    return v