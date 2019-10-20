import random
import game
import sys
import numpy as np
import os

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.
"""
	1400
	3424
	5880
	2356
	3568
	3844
	5724
	2424
	3036
	3152
	6544
	5584
	3352
	6216
	3500
Average:	4000,266667
/*Game over. Final score 6376; highest tile 512.
Game over. Final score 1544; highest tile 128.
Game over. Final score 1328; highest tile 128.
Game over. Final score 3584; highest tile 256.
Game over. Final score 3220; highest tile 256.
Game over. Final score 7252; highest tile 512.
Game over. Final score 3548; highest tile 256.
Game over. Final score 4360; highest tile 256.
Game over. Final score 1760; highest tile 128.
Game over. Final score 2860; highest tile 256.*/
"""

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

lastboard = np.array([[0]*4 for _ in range(4)])
lastmove = -1
lastlastmove = -1

cntMoves = 0
cntUPMoves = 0

maxSameMoves = 2

filename = os.path.basename(__file__)

def find_best_move(board):
    bestmove = -1    
	
	# TODO:
	# Build a heuristic agent on your own that is much better than the random agent.
	# Your own agent don't have to beat the game.
    
    global lastboard
    global lastmove
    global lastlastmove
    global cntMoves

    global cntUPMoves

    if cntMoves <= 6:
        if lastmove == DOWN:
            bestmove = RIGHT
        else:
            bestmove = DOWN
        cntMoves += 1
    else:
        if board_equals(board, lastboard) and ((lastmove == RIGHT and lastlastmove == DOWN) or (lastmove == DOWN and lastlastmove == RIGHT)):
            bestmove = LEFT
        elif board_equals(board, lastboard) and lastmove == LEFT:
            bestmove = UP
            cntUPMoves += 1
        elif lastmove == LEFT:
            if isBottomRowFull(board):
                bestmove = DOWN
            else:
                bestmove = RIGHT
        elif lastmove == UP:
            bestmove = DOWN
        elif board_equals(board, lastboard) and (lastmove == DOWN):
            bestmove = RIGHT
        elif board_equals(board, lastboard) and (lastmove == RIGHT):
            bestmove = DOWN
        elif lastmove == DOWN and lastlastmove == DOWN:
            bestmove = RIGHT
        elif lastmove == RIGHT and lastlastmove == RIGHT:
            bestmove = DOWN
        elif lastmove == RIGHT:
            bestmove = RIGHT
        else:
            bestmove = DOWN
    
    lastboard = board
    lastlastmove = lastmove
    lastmove = bestmove
    #print(cntUPMoves)
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