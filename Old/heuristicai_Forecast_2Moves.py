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
    highscore = 0;
    newboard = np.array([0])
    second_highscore = 0

    for i in range (0,4):
        newboard = execute_move(i,board)
        if not board_equals(board, newboard):
            second_highscore = 0
            for j in range (0,4):
                newboard_second_move = execute_move(j,board)
                score = get_boardscore(newboard) 
                if score > second_highscore and not board_equals(newboard, newboard_second_move):
                    second_highscore = score

        if second_highscore > highscore:
            highscore = second_highscore
            bestmove = i

    return bestmove

def find_best_move_random_agent():
    return random.choice([UP,DOWN,LEFT,RIGHT])
    
def double_move(move):


    return score

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
            score += board[i, j] * (i + 4) *(j + 1) 
            
    return score
    
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  
