import tictactoe as ttt
X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, X],
        [O, O, EMPTY],
        [X,  EMPTY, O]]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if ttt.terminal(board): #game over
        return None
    
    elif ttt.player(board)==X:
        plays=[]

        for action in ttt.actions(board):
            plays.append([ttt.min_value(ttt.result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    
    elif ttt.player(board)==O:
        plays=[]

        for action in ttt.actions(board):
            plays.append([ttt.max_value(ttt.result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]
    
print(minimax(board))