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
        #print(cntMoves)
    else:
        if lastmove == RIGHT or lastmove == DOWN:
            bestmove = getBestMoveByScoringMoves(board)
        if bestmove == -1:
            bestmove = getBestMoveDependingOnPreviousMove(board)
            #print("prev move: ", bestmove)

    lastboard = board
    lastlastmove = lastmove
    lastmove = bestmove
    #print(cntUPMoves)
    return bestmove

def getBestMoveDependingOnPreviousMove(board):
    if board_equals(board, lastboard) and (
            (lastmove == RIGHT and lastlastmove == DOWN) or (lastmove == DOWN and lastlastmove == RIGHT)):
        bestmove = LEFT
    elif board_equals(board, lastboard) and lastmove == LEFT:
        bestmove = UP
    elif lastmove == LEFT and isBottomRowFull(board):
        bestmove = DOWN
    elif lastmove == LEFT:
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
    return bestmove

def getScoreNextRound(board, move):
    new_board = execute_move(move, board)
    secondscore = 0
    if (not board_equals(board, new_board)):
        secondscore = getScoreForMoveDown(new_board)
        temp = getScoreForMoveRight(new_board)
        if (temp > secondscore):
            secondscore = temp
        temp += getScoreForMoveLeft(new_board)
        if (temp > secondscore):
            secondscore = temp
        temp += getScoreForMoveUp(new_board)
        if (temp > secondscore):
            secondscore = temp
    return secondscore

def getBestMoveByScoringMoves(board):
    bestmove = -1
    threshold = 40

    score = getScoreForMoveDown(board) + getScoreNextRound(board, DOWN)
    if (score >= threshold):
        bestmove = DOWN

    scoreNew = getScoreForMoveRight(board) + getScoreNextRound(board, RIGHT)
    if (score < scoreNew):
        score = scoreNew
        if (score >= threshold):
            bestmove = RIGHT

    scoreNew = getScoreForMoveLeft(board) + getScoreNextRound(board, LEFT)
    if (score < scoreNew):
        score = scoreNew
        if (score >= threshold):
            bestmove = LEFT

    scoreNew = getScoreForMoveUp(board) + getScoreNextRound(board, UP)
    if (score*2 < scoreNew):
        score = scoreNew
        if (score >= threshold):
            bestmove = UP

    #print("bestscore", score, bestmove)
    return bestmove

def getScoreForMoveRight(board):
    skipNext = False
    score = 0;
    for i in range(4):
        for j in range(2,-1,-1): # count 2, 1, 0
            if skipNext:
                skipNext = False
                continue
            if (board[i,j] == board[i,j+1]):
                skipNext = True
                score += board[i,j]*2*i*i
    return score

def getScoreForMoveLeft(board):
    skipNext = False
    score = 0;
    for i in range(4):
        for j in range(1,4): # count 1, 2, 3
            if skipNext:
                skipNext = False
                continue
            if (board[i,j] == board[i,j-1]):
                skipNext = True
                score += board[i,j]*2*i
    if not isBottomRowFull(board) or isBottomRowMergeable(board):
        score /= 2

    return score

def getScoreForMoveDown(board):
    skipNext = False
    score = 0;
    for i in range(4):
        for j in range(2,-1,-1): # count 2, 1, 0
            if skipNext:
                skipNext = False
                continue
            if (board[j,i] == board[j+1,i]):
                skipNext = True
                score += board[j,i]*2*(j+1)*(j+1)

    return score

def getScoreForMoveUp(board):
    skipNext = False
    score = 0;
    for i in range(4):
        for j in range(1,4): # count 1, 2, 3
            if skipNext:
                skipNext = False
                continue
            if (board[j,i] == board[j-1,i]):
                skipNext = True
                score += board[j,i]*2*(j-1)
    if not isRightColFull(board) or isRightColMergeable(board):
        score /= 2

    return score

def isBottomRowMergeable(board):
    mergeable = False
    for i in range(1,4):
        if (board[3,i] != 0 and board[3,i] == board[3,i-1]):
            mergeable = True
            break;
    return mergeable

def isRightColMergeable(board):
    mergeable = False
    for i in range(1,4):
        if (board[i,3] != 0 and board[i,3] == board[i-1,3]):
            mergeable = True
            break;
    return mergeable

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

#def find_best_move_horizonal_pair(board):
#    for i in range(4):
#        if (board)
#    return random.choice([UP,DOWN,LEFT,RIGHT])

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