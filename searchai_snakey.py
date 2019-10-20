import os
import random
import game
import sys
import numpy as np

#import heuristicai as ai
import time
import multiprocessing as mp

# Author: chrn (original by nneonneo)
# Date: 11.11.2016
# Copyright: Algorithm from https://github.com/nneonneo/2048-ai
# Description: The logic to beat the game.  Based on expectimax algorithm.
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
move_args = [UP,DOWN,LEFT,RIGHT]

#snakescore = np.array([[4,3,2,1],
#                 [8,6,7,8],
#                 [15,14,13,12],
#                 [18,19,20,21]])**4
snakescore = np.array([[4,3,2,1],
                  [5,6,7,8],
                  [12,11,10,9],
                  [13,14,15,16]])**4

filename = os.path.basename(__file__)

def find_best_move(board):
    """
    find the best move for the next turn.
    """
    global p
    bestmove = -1

    emptyTiles = countEmptyTiles(board)
    biggestTile = getHighestTile(board)
    start = time.time()
    if emptyTiles > 8 or biggestTile < 1024:
        result = [score_toplevel_move(x, board, 1) for x in range(len(move_args))]
    elif emptyTiles > 4 or biggestTile < 2048:
        result = []
        r = []  
        for x in range(len(move_args)):
            r.append(p.apply_async(score_toplevel_move, (x, board, 2)))
        for i in range(len(r)):
            result.append(r[i].get())
    else:
        result = []
        r = []  
        for x in range(len(move_args)):
            r.append(p.apply_async(score_toplevel_move, (x, board, 3)))
        for i in range(len(r)):
            result.append(r[i].get())

    bestmove = result.index(max(result))
    """for m in move_args:
        print("move: %d score: %.4f" % (m, result[m]))
    print("Time needed = ", time.time() - start)"""
    
    if max(result) == 0: # Every move leads to game over --> finish game
        bestmove = random.choice([UP,DOWN,LEFT,RIGHT])
    
    return bestmove

def countEmptyTiles(board):
    return np.count_nonzero(board == 0)

def getHighestTile(board):
    return np.max(board)

def score_toplevel_move(move, board, depth=2):
    """
    Entry Point to score the first move.
    """
    newboard = execute_move(move, board)
    
    if board_equals(board,newboard):
        return 0
	# TODO:
	# Implement the Expectimax Algorithm.
	# 1.) Start the recursion until it reach a certain depth
	# 2.) When you don't reach the last depth, get all possible board states and
	#		calculate their scores dependence of the probability this will occur.
	#		(recursively)
	# 3.) When you reach the leaf calculate the board score with your heuristic.

    #print(str(depth) + " move: " + str(move))
    if depth == 0:
        return getScore(newboard)
    
    score = 0
    depth -= 1
    cntEmptyFields = 0
    for i in range(4):
        for j in range(4):
            if newboard[i,j] != 0:
                continue
            cntEmptyFields += 1
            newboard[i,j] = 2
            maxscore = max([score_toplevel_move(m, np.copy(newboard), depth) for m in range(len(move_args))])
            score += 0.9 * maxscore

            newboard[i,j] = 4
            maxscore = max([score_toplevel_move(m, np.copy(newboard), depth) for m in range(len(move_args))])
            score += 0.1 * maxscore

            newboard[i,j] = 0
    if score == 0:  # no further moves
        return 0 # return 0 as this move leads into game over
    else:
        cntEmptyFields = max(1,cntEmptyFields)
        return score / cntEmptyFields

def getScore(board):
    return np.sum(np.multiply(board,snakescore));

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

def main():
    global p
    p = mp.Pool(4)

if __name__ == "__main__":
    main()
