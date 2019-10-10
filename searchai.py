import random
import game
import sys
import numpy as np
import heuristicai as heuristic

# Author: chrn (original by nneonneo)
# Date: 11.11.2016
# Copyright: Algorithm from https://github.com/nneonneo/2048-ai
# Description: The logic to beat the game.  Based on expectimax algorithm.
def find_best_move(board):
    """
    find the best move for the next turn.
    """
    bestmove = -1
    depth = 2
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    move_args = [UP,DOWN,LEFT,RIGHT]
    
    result = [score_toplevel_move(i, board, depth) for i in range(len(move_args))]
    bestmove = result.index(max(result))

    for m in move_args:
        print("move: %d score: %.4f" % (m, result[m]))

    return bestmove
    
def score_toplevel_move(move, board, depth):
    """
    Entry Point to score the first move.
    """
    newboard = execute_move(move, board)
    
    if board_equals(board,newboard) or depth == 0:
        return 0
	# TODO:
	# Implement the Expectimax Algorithm.
	# 1.) Start the recursion until it reach a certain depth
	# 2.) When you don't reach the last depth, get all possible board states and
	#		calculate their scores dependence of the probability this will occur.
	#		(recursively)
	# 3.) When you reach the leaf calculate the board score with your heuristic.
    depth -= 1
    spawnNr = (newboard == 0).sum() * 2
    spawnsPossibility = np.array[(spawnNr)]

    for i in range(0, spawnNr):
        probability = i
        score_toplevel_move(i, board, depth)
        
    return random.randint(1,1000)

def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

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
