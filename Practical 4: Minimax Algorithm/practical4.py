#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:15:12 2020

CS310 Foundations of Artificial Intelligence
Practical 4: Minimax Algorithm
@author: jamesodonnell
"""

import math
import time

# minimax_run(state) is the main function for running the game.
# test_timing((state)) will run the main function and time it for comparison with practical 5

def minimax_run(state):
    
    moves = [state]
      
    # While not terminal state
    while(next_state(state) != None):
        state = next_state(state)
        moves.append(state)
        if (moves[-1][0] == []):
            print("Example play:") 
            for x in range(0, len(moves)):
                print(moves[x])
    print("Value:", minimax_value(moves[-1]))
     

def minimax_value(state):
    # MAX win
    if(state == ([],1)):
        return 1
    
    # MIN win
    if(state == ([],2)):
        return -1
    
    # Deepen
    if(state[1] == 1):
        best_score = -math.inf
        next_states = successors(state)
        for x in range(0, len(next_states)):
            value = minimax_value(next_states[x])
            best_score = max(best_score, value)
        return best_score
    
    # Deepen
    else:
        best_score = math.inf
        next_states = successors(state) 
        for i in range(0, len(next_states)):
            value = minimax_value(next_states[i])
            best_score = min(best_score, value)
        return best_score
    
def next_state(state):
    # Terminal
    if(state[0] == []):
        return None
    # Deepen
    if(state[1] == 1):
        best_score = -math.inf
        best_move = 0
        next_states = successors(state)
        for x in range(0, len(next_states)):
            value = minimax_value(next_states[x])
            if(value > best_score):
                best_score = value
                best_move = x
        return next_states[best_move]
    # Deepen
    else:
        best_score = math.inf
        best_move = 0
        next_states = successors(state)
        for x in range(0, len(next_states)):
            value = minimax_value(next_states[x])
            if (value < best_score):
                best_score = value
                best_move = x
        return next_states[best_move]
    
# Returns all possible successor moves
def successors(state):
    piles = []
    final = [[]]
    p = (state[1] % 2) + 1
    for s in state[0]:
        piles.append(s)
    for i in range(0,len(piles)):
        element = piles[i]
        index = i
        if element == 3:
            possible = [1,2,0]
            for j in range (0,len(possible)):
                result = []
                if index != 0:
                    for y in range(0, index):
                        result.insert(y,piles[y])
                if j != 2:
                    result.append(possible[j])
                if index != (len(piles)-1):
                    for x in range(index+1,len(piles)):
                        result.insert(x,piles[x])
                if (result,p) not in final:
                    final.append((result,p))
        if element == 2:
            possible = [1,0]
            for j in range (0,len(possible)):
                result = []
                if index != 0:
                    for y in range(0, index):
                        result.insert(y,piles[y])
                if j == 0:
                    result.append(possible[j])
                if index != (len(piles)-1):
                    for x in range(index+1,len(piles)):
                        result.insert(x,piles[x])
                if (result,p) not in final:
                    final.append((result,p))
        if element == 1:
            result = []
            if index != 0:
                for y in range(0, index):
                    result.insert(y,piles[y])
            if index != (len(piles)-1):
                for x in range(index+1,len(piles)):
                    result.insert(x,piles[x])
            if (result,p) not in final:
                    final.append((result,p))
        if element > 3:
            possible = [element-1,element-2,element-3]
            for j in range (0,len(possible)):
                result = []
                if index != 0:
                    for y in range(0, index):
                        result.insert(y,piles[y])
                result.append(possible[j])
                if index != (len(piles)-1):
                    for x in range(index+1,len(piles)):
                        result.insert(x,piles[x])
                if (result,p) not in final:
                    final.append((result,p))
    final.pop(0)
    return (final)

# Tests time taken for comparison with practical 5
def test_timing(state):
    
    # Remove prints for ([5,5,5], 1)
    
    start = time.time()
    value = minimax_run(state)
    end = time.time()
    final = end - start
    print("Time taken:", final)
    return value


    