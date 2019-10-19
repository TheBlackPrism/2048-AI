import os
import random
import game
import sys
import numpy as np

# Author: chrn (original by nneonneo)
# Date: 11.11.2016
# Description: The logic of the AI to beat the game.
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

filename = os.path.basename(__file__)

def find_best_move(board):
    bestmove = -1 
    highscore = 0
    newboard = np.array([0])

    for i in range(0,4):
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

    for i in range(0,4):
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

    for y in range(0,4):
        for x in range(0,4):
            factoredgex = 1
            factoredgey = 1

            neighbourbonus = get_neighbour_bonus(x,y,board)
            edgebonus = get_edge_distance_bonus(x,y,board)

            if board[y,x] != 0:
                score += board[y, x] * neighbourbonus * edgebonus
            else:
                score += 20 * (4 - x) * (6 - y) # Reward empty Fields according to their position on the board

    return score

def get_edge_distance_bonus(x, y, board):
    bonus = 1

    if y == 3:
        if x == 3:
            bonus *= 100 # Bottom right corner bonus
        else:
            bonus = 10 * (x + 4)
    elif y == 2:
        bonus = 5 * (4 - x)
    elif y == 1:
        bonus = 2 * (x + 4)

    return bonus

def get_neighbour_bonus(x, y, board):
    bonus = 1
    if y > 0 and board[y - 1, x] == board[y, x]:
        bonus *= 2
    if x > 0 and board[y, x - 1] == board[y, x]:
        bonus *= 2

    return bonus

def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  