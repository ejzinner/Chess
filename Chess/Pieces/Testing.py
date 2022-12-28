# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 16:22:22 2022

@author: ejzin
"""
from chess.pieces.rook import Rook

board = {(rank, file): False for rank in range(8) for file in range(8)}
board[(4, 4)] = Rook((4,4), 'white')
board[(6, 4)] = Rook((6,4), 'white')
board[(4, 7)] = Rook((4,7), 'black')

myPiece = board[(4, 4)]
legalMoves = myPiece.legalMoves()
print(legalMoves)