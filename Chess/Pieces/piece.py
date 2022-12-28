# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:13:10 2022

@author: ejzinner
"""
from abc import ABC, abstractMethod
class Piece:
    position: ()
    color: bool
    hasMoved: bool

def __init__(self, location, color, hasMoved = False):
    self.location = location
    self.color = color
    self.hasMoved = hasMoved
    

@abstractMethod
def legalMoves():
    pass

@abstractMethod
def squaresDefended():
    pass

@abstractMethod
def getName():
    pass

def getRank(self):
    return self.position[1]

def getFile(self):
    return self.position[0]



    

 
    
    