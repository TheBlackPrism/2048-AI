import random
import game
import sys
import numpy as np

# Author:				chrn (original by nneonneo)
# Date:				    11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

lastmove = 2
lastboard = np.array([1])
triedboth = False
startphase = True

def find_best_move(board):
    bestmove = -1    

    global lastmove
    global lastboard
    global triedboth
    global startphase

    if startphase:
        if lastmove == LEFT:
            bestmove = UP
        else:
            bestmove = LEFT
    else:
        if board_equals(lastboard, board) and triedboth:
            if triedboth:
                if lastmove == DOWN:
                    bestmove = RIGHT
                elif (row_full(board[0]) and not row_full(board[:,0])): #or (row_score(board[0]) >= row_score(board[:,0]) and (row_full(board[0]) or not row_full(board[:,0]))):
                    bestmove = DOWN
                else:
                    bestmove = RIGHT
                triedboth = False

        elif lastmove == LEFT:
            if not board_equals(lastboard, board):
                bestmove = LEFT
            else:
                bestmove = UP
        elif lastmove == UP:
            bestmove = LEFT
        elif lastmove == DOWN:
                bestmove = UP
        elif lastmove == RIGHT:
                bestmove = LEFT
        
    if board_equals(lastboard, board) and not triedboth:
        triedboth = True
        startphase = False
    elif not board_equals(lastboard, board) and triedboth:
        triedboth = False

    lastboard = board
    lastmove = bestmove
    return bestmove

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

def row_full(row):
    count = 0
    for cell in row:
        if cell == 0:
            count += 1
    return count == 0

def row_score(row):
    score = 0
    for cell in row:
        score += cell
    return score
    
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  
