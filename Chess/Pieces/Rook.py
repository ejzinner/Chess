# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:30:04 2022

@author: ejzin
"""

from chess.pieces.piece import Piece
class Rook(Piece):
    pieceName: str
    position: ()
    color: bool
    hasMoved: bool
def __init__(self, position, color, hasMoved = False):
    super(position, color, hasMoved)
    
#def possibleMoves():
# =============================================================================
#     possibleMoves = []
#     rank = self.getRank()
#     file = self.getFile()
#     for newRank in range(8):
#         if newRank == rank:
#             continue
#         possibleMoves.append((file, newRank))
#     for newFile in range(8):
#         if newFile == file:
#             continue
#         possibleMoves.append((newFile, rank))
#     return possibleMoves
# =============================================================================
    
def legalMoves(self, possibleMoves, board):
    rank = self.getRank()
    file = self.getFile()
    legalMoves = []
    for newRank in range(rank+1, 8):
        position = (newRank, file)    
        if board[position] == False: #It's empty, so this is fine, rook can keep moving
            legalMoves.append(position)
        elif not board.position.color == self.color: #there is an opponent piece, we can move here but no further
            legalMoves.append(position)
            break
        else: #my piece is here, I cannot move here or past it
            break
    
    for newRank in range(rank-1, -1, -1):
        position = (newRank, file)    
        if board[position] == False: #It's empty, so this is fine, rook can keep moving
            legalMoves.append(position)
        elif not board.position.color == self.color: #there is an opponent piece, we can move here but no further
            legalMoves.append(position)
            break
        else: #my piece is here, I cannot move here or past it
            break
        
    for newFile in range(file+1, 8):
        position = (rank, newFile)    
        if board[position] == False: #It's empty, so this is fine, rook can keep moving
            legalMoves.append(position)
        elif not board.position.color == self.color: #there is an opponent piece, we can move here but no further
            legalMoves.append(position)
            break
        else: #my piece is here, I cannot move here or past it
            break
        
    for newFile in range(file-1, -1, -1):
        position = (rank, newFile)    
        if board[position] == False: #It's empty, so this is fine, rook can keep moving
            legalMoves.append(position)
        elif not board.position.color == self.color: #there is an opponent piece, we can move here but no further
            legalMoves.append(position)
            break
        else: #my piece is here, I cannot move here or past it
            break
        
def getName():
    return 'Rook'

board = {(rank, file): False for rank in range(8) for file in range(8)}
board[(4, 4)] = Rook((4,4), 'white')
board[(6, 4)] = Rook((6,4), 'white')
board[(4, 7)] = Rook((4,7), 'black')

myPiece = board[(4, 4)]
legalMoves = myPiece.legalMoves()
print(legalMoves)