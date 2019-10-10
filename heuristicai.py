import random
import game
import sys
import numpy as np

# Author:				chrn (original by nneonneo)
# Date:				    11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
    bestmove = -1 
    highscore = 0
    newboard = np.array([0])

    for i in range (0,4):
        newboard = execute_move(i, board)
        score = get_boardscore(newboard)

        if not board_equals(board, newboard):
            score += double_up(board)
            if score > highscore:
                highscore = score
                bestmove = i

    return bestmove

def double_up(board):
    highscore = 0
    newboard = np.array([0])

    for i in range (0,4):
        newboard = execute_move(i, board)
        score = get_boardscore(newboard)
        if score > highscore and not board_equals(board, newboard):
            highscore = score

    return highscore

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

def get_boardscore(board):
    score = 0

    for i in range (0,4):
        for j in range (0,4):
            factorx = 1
            factory = 1
            factoredgex = 1
            factoredgey = 1

            if i > 0 and board[i-1, j] == board[i, j]:
                factorx = 3   
            if j > 0 and board[i, j-1] == board[i,j]:
                factory = 3
            if i == 3:
                factoredgex = 4
            if j == 3:
                factoredgey = 2

            if board[i,j] != 0:
                score += board[i, j]  * factorx * factory * (factoredgex + i + 1) * (factoredgey + j + 2)
            else:
                score += 4000
    return score
    
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  
