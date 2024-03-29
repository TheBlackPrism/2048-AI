#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: chrn (original by nneonneo)
# Date: 11.11.2016, updated by scik 30.08.2019
# Copyright: https://github.com/nneonneo/2048-ai
# Description: Helps the user achieve a high score in a real game of 2048 by
# using a move searcher.
#              This Script initialize the AI and controls the game flow.


#from __future__ import print_function
import time

#import heuristicai_yves as ai #for task 4
import searchai_snakey as ai #for task 5
#import heuristicai_SOLUTION as ai #for task 4
                     #import searchai_SOLUTION as ai #for task 5
def print_board(m):
    for row in m:
        for c in row:
            print('%8d' % c, end=' ')
        print()

def _to_val(c):
    if c == 0: return 0
    return c

def to_val(m):
    return [[_to_val(c) for c in row] for row in m]

def _to_score(c):
    if c <= 1:
        return 0
    return (c - 1) * (2 ** c)

def to_score(m):
    return [[_to_score(c) for c in row] for row in m]

def find_best_move(board):
    return ai.find_best_move(board)

def movename(move):
    return ['up', 'down', 'left', 'right'][move]

def play_game(gamectrl):
    moveno = 0
    start = time.time()
    while 1:
        state = gamectrl.get_status()
        if state == 'ended':
            break
        elif state == 'won':
            time.sleep(0.75)
            gamectrl.continue_game()

        moveno += 1
        board = gamectrl.get_board()
        move = find_best_move(board)
        if move < 0:
            break
        """print("%010.6f: Score %d, Move %d: %s" % (time.time() - start, gamectrl.get_score(), moveno, movename(move)))"""
        gamectrl.execute_move(move)

    score = gamectrl.get_score()
    board = gamectrl.get_board()
    maxval = max(max(row) for row in to_val(board))
    timepermove = (time.time() - start) / moveno
    print("Game over. Final score %d; highest tile %d." % (score, maxval))
    print("Number of Moves %d; Time per Move %f" % (moveno, timepermove))
    print("The board: ")
    print(board)
    writeCSV(score, maxval, moveno, timepermove)

def parse_args(argv):
    import argparse

    parser = argparse.ArgumentParser(description="Use the AI to play 2048 via browser control")
    parser.add_argument('-p', '--port', help="Port number to control on (default: 32000 for Firefox, 9222 for Chrome)", type=int)
    parser.add_argument('-b', '--browser', help="Browser you're using. Only Firefox with the Remote Control extension, and Chrome with remote debugging (default), are supported right now.", default='chrome', choices=('firefox', 'chrome'))
    parser.add_argument('-k', '--ctrlmode', help="Control mode to use. If the browser control doesn't seem to work, try changing this.", default='hybrid', choices=('keyboard', 'fast', 'hybrid'))

    return parser.parse_args(argv)

def main(argv):
    args = parse_args(argv)

    if args.browser == 'firefox':
        from ffctrl import FirefoxRemoteControl
        if args.port is None:
            args.port = 32000
        ctrl = FirefoxRemoteControl(args.port)
    elif args.browser == 'chrome':
        from chromectrl import ChromeDebuggerControl
        if args.port is None:
            args.port = 9222
        ctrl = ChromeDebuggerControl(args.port)

    # if args.ctrlmode == 'keyboard':
    #     from gamectrl import Keyboard2048Control
    #     gamectrl = Keyboard2048Control(ctrl)
    # elif args.ctrlmode == 'fast':
    #     from gamectrl import Fast2048Control
    #     gamectrl = Fast2048Control(ctrl)
    # elif args.ctrlmode == 'hybrid':
    #     from gamectrl import Hybrid2048Control
    #     gamectrl = Hybrid2048Control(ctrl)

    from gamectrl import Fast2048Control
    gamectrl = Fast2048Control(ctrl)

    if gamectrl.get_status() == 'ended':
        gamectrl.restart_game()

    play_game(gamectrl)
    return gamectrl

csv_file = "out.csv"
def createCSV():
    global csv_file
    csv_file = "stats_" + ai.filename + "_" + str(int(time.time())) + ".csv"
    try:
        f = open(csv_file, "w")
    except IOError:
        print("Cannot open file " + csv_file)
    else:
        with f:
            data = "score;highest tile;number of moves;time per move\n"
            f.write(data)

def writeCSV(score, maxval, moveno, time):
    try:
        f = open(csv_file, "a")
    except IOError:
        print("Cannot open file " + csv_file)
    else:
        with f:
            data = "%d; %d; %d; %f \n" % (score, maxval, moveno, time)
            f.write(data)

if __name__ == '__main__':
    import sys
    times = 10
    total = 0
    highscore = 0
    
    print("Starting Game...")
    print("Filename: %s" % (ai.filename))
    print("************************")
    createCSV()

    arglength = len(sys.argv)
    try:
        ai.main()
    except AttributeError:
        pass # Method doesn't exist

    if arglength > 3:
        times = int(sys.argv[arglength - 1])
        sys.argv = sys.argv[0:arglength - 3]

    for i in range(0, times):
        game = main(sys.argv[1:])

        score = game.get_score()
        total += score
        if score > highscore:
            highscore = score

    print("************************\n")
    print("Nr of tries:\t%d\nHighscore:\t%d\nAverage Score:\t%d\n\n" % (times, highscore, (total / times)))