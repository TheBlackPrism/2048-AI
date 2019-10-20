import random
import game
import sys
import numpy as np
import os

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

lastboard = np.array([[0]*4 for _ in range(4)])
lastmove = -1

filename = os.path.basename(__file__)

def find_best_move(board):
    bestmove = -1    
	
	# TODO:
	# Build a heuristic agent on your own that is much better than the random agent.
	# Your own agent don't have to beat the game.
    
    global lastboard
    global lastmove
    
    if board_equals(board, lastboard):
        if isBottomRowFull(board) and lastmove != LEFT:
            bestmove = LEFT
        elif isRightColFull(board) and lastmove != UP:
            bestmove = UP
        elif lastmove == LEFT:
            bestmove = UP
        else:
            bestmove = LEFT
    else:
        if lastmove == RIGHT:
            bestmove = DOWN
        else:
            bestmove = RIGHT

    lastboard = board
    lastmove = bestmove
    return bestmove

def isBottomRowFull(board):
    full = True
    for i in range(4):
        if (board[3,i] == 0):
            full = False
    return full

def isRightColFull(board):
    full = True
    for i in range(4):
        if (board[i,3] == 0):
            full = False
    return full

def find_best_move_random_agent():
    return random.choice([UP,DOWN,LEFT,RIGHT])
    
def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")
		
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  