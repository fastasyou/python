# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:40:07 2018

@author: bob
"""

#import matplotlib.pyplot as plt
import numpy as np
import random
#plt.subplot(333) 
#plt.subplot(3, 3, 3)
def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    if board[position]==0:
        board[position]=player

def possibilities(board):
    placements = []
    a = np.where(board==0)
    for i in range(len(a[0])):
        placements.append((a[0][i],a[1][i]))
    return placements
    
def random_place(board, player):
    placements = possibilities(board)
    placement = random.choice(placements)
    place(board, player, placement)

def win(board, player):
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return True
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        return True
    for i in range(3):
         if board[i][0]==player and board[i][1]==player and board[i][2]==player:
             return True
    for i in range(3):
         if board[0][i]==player and board[1][i]==player and board[2][i]==player:
             return True
    return False

def row_win(board, player):
    for i in range(3):
         if board[i][0]==player and board[i][1]==player and board[i][2]==player:
             return True
    return False

def col_win(board, player):
    for i in range(3):
         if board[0][i]==player and board[1][i]==player and board[2][i]==player:
             return True
    return False
def diag_win(board, player):
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        return True
    if board[0][2]==player and board[1][1]==player and board[2][0]==player:
        return True
    return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply. 
		# If so, store `player` as `winner`.
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# add your code here.

def play_game():
    board = create_board()
    result=0
    while(True):
        for player in [1, 2]:
            random_place(board, player)
            result = evaluate(board)
            if result==1 or result==2 or result ==-1:
                return result

print(play_game())

#place(board, 1, (0,1))
#place(board, 1, (1,1))
#place(board, 1, (2,1))
#board = create_board()
#random_place(board, 2)
#print(board)
#print(row_win(board,1))
#
#print(evaluate(board))