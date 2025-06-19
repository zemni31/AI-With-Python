"""
Tic Tac Toe Player
"""

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
    nbX=0
    nbO=0
    
    for row in board :
        for cell in row:
            if cell==X:
                nbX+=1
            elif cell==O:
                nbO+=1
    if nbX>nbO:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()
    for i in range(3):
      for j in range(3):
          if board[i][j] == EMPTY: 
              actions.add((i,j))
    return actions
           

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]
    if action not in actions(board):
        raise Exception("Action non disponible")
    i,j=action
    new_board[i][j]=player(board)
    return new_board

def winner(board):
       """
       Returns the winner of the game, if there is one.
       """
  
       for i in range(3):
           if (all(board[i][j] == X for j in range(3)) or all(board[j][i] == X for j in range(3))):
               return X
       if (all(board[i][i] == X for i in range(3)) or
           all(board[i][2 - i] == X for i in range(3))):
           return X
       for i in range(3):
           if (all(board[i][j] == O for j in range(3)) or all(board[j][i] == O for j in range(3))):
               return O
       if (all(board[i][i] == O for i in range(3)) or
           all(board[i][2 - i] == O for i in range(3))):
           return O
       return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    # Si toutes les cases sont remplies
    for row in board:
        if EMPTY in row:
            return False
    return True

  

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    if(player(board)==X):
        value,move=max_value(board)
    else:
        value,move=min_value(board)
    return move
        
def max_value(board):
    """
    Returns the maximum value of the board for player X.
    """
    if(terminal(board)):
        return utility(board),None
    v=float('-inf')
    best_action=None
    for action in actions(board):
        min,_=min_value(result(board,action))
        if min>v:
            v=min
            best_action=action
    return v,best_action

def min_value(board):
    """
    Returns the minimum value of the board for player O.
    """
    if(terminal(board)):
        return utility(board),None
    v=float('inf')
    best_action=None
    for action in actions(board):
        max,_=max_value(result(board,action))
        if max<v:
            v=max
            best_action=action
    return v,best_action

    
  
        

    

    


