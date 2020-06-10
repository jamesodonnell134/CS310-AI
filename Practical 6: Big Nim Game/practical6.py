    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 5 20:09:17 2020

CS310 Foundations of Artificial Intelligence
Practical 6: Big Nim
@author: jamesodonnell
"""

import math
import random
import time

transposition_table = {}

# Main function for playing nim
def play():
    
    piles = []
    print("Let's play nim!")
    
    noPiles = int(input("How many piles initially? : "))
    noSticks = int(input("Maximum number of sticks? : "))
    
     # Generating a random start state
    for x in range(0, noPiles):
        piles.append(random.randint(1, noSticks))
    print("\nThe initial state is : ", piles)

    play = int(input("Do you want to go first (1), second (2) or AI vs AI (3)? : "))
        
    while(play <= 0 or play > 3):
        play = int(input("Invalid input. Do you want to go first (1), second (2) or AI vs AI (3)? : "))
    
    if(play == 1):
        human_vs_ai(piles, 1)
        
    if(play == 2):
        human_vs_ai(piles, 2)

    if(play == 3):
        ai_vs_ai(piles)
        
# Play against AI
def human_vs_ai(piles, player):
    print("\n====================")
    print("==== YOU vs AI! ====")
    print("====================")

    state = (piles, player)
    while(state[0] != []):
        
        # Your turn
        if(state[1] == 1):
            print("\nYour turn. State is : ",state[0])
            pile = 0
            if(len(state[0]) > 1):
                pile = int(input("Which pile do you want to remove a stick from? : "))
                
                while(pile <= 0 or pile > len(state[0])):
                    print("Pile out of range! There are",len(piles),"piles. Choose a number between 1 and",len(piles),".")
                    pile = int(input("Which pile do you want to remove a stick from? : "))
                pile -=1
            sticks = int(input("Remove how many sticks? : "))
            
            while(sticks <= 0 or sticks > 3 or sticks > state[0][pile]):
                print("Sticks out of range! You can only remove 1-3 sticks at a time.")
                sticks = int(input("Remove how many sticks? : "))

            updated_pile = (state[0].copy())
            remove = (updated_pile.pop(pile))
            remove -= sticks

            # Don't add to pile if all sticks taken
            if(remove > 0):
                updated_pile.insert(pile, remove)
            state = (updated_pile.copy(), 2)
            
        # AI's turn
        else:
            print("\nAI's turn. State is : ",state[0])
            state = next_state(state)
            
    if(minimax_value(state) == 1):
       print("\nThe winner is: YOU! :)")
        #print (transposition_table)
    else:
       print("\nThe winner is: AI :(")
        #print (transposition_table)
          
# AI plays self
def ai_vs_ai(piles):
    print("\n===================")
    print("==== AI vs AI! ====")
    print("===================")
    
    state = (piles, 1)
    
    while(state[0] != []):
        if(state[1] == 1):
            print("MAX player's turn. State is : ",state[0])
            state = next_state(state)
        else:
            print("MIN player's turn. State is : ",state[0])
            state = next_state(state)
    if(minimax_value(state) == 1):
        print("\nThe winner is: MAX!")
        #print (transposition_table)
    else:
        print("\nThe winner is: MIN!")
        #print (transposition_table)
    
# ==========================================================
# ========= Functions used from Practicals 4 and 5 =========
# ==========================================================

    
def test_timing(piles):
        
    start = time.time()
    value = ai_vs_ai(piles)
    end = time.time()
    final = end - start
    print("Time taken:", final)
    return value


# Computes the maximum value with alpha beta pruning
def maxvalue_prune (state, alpha, beta):
    if(state[0] == []):
        return 1
    # No need to deepen, retrieve from dictionary
    if(str(state[0]) in transposition_table):
        return transposition_table[str(state[0])]
    
    value = -math.inf
    next_states = successors(state)
    
    for s in next_states:
        vnew = minvalue_prune(s, alpha, beta)
        value = max(vnew, value)
        if(vnew >= beta):
            #prn = "beta pruning at", state, "with alpha = ", alpha, "and beta = ", beta
            #if prn not in prinArr:
                #prinArr.append(prn)
            transposition_table[str(state[0])] = value
            return value
        alpha = max(alpha, vnew)
        
    # Add to dictionary 
    transposition_table[str(state[0])] = value
    return value
  
# Computes the minimum value with alpha beta pruning      
def minvalue_prune (state, alpha, beta):
    if(state[0] == []):
        return -1
    # No need to deepen, retrieve from dictionary
    if(str(state[0]) in transposition_table):
        return transposition_table[str(state[0])] * -1
    
    value = math.inf
    next_states = successors(state)
    
    for s in next_states:
        vnew = maxvalue_prune(s, alpha, beta)
        value = min(vnew, value)
        if(vnew <= alpha):
            #prn = "alpha pruning at", state, "with alpha = ", alpha, "and beta = ", beta
            #if prn not in prinArr:
                #prinArr.append(prn)
                transposition_table[str(state[0])] = -value
                return value
        beta = min(beta, vnew)
        
    # Add to dictionary
    transposition_table[str(state[0])] = -value
    return value

            
def next_state(state):
    # If terminal state
    if(state[0] == []):
        return None
    alpha = -math.inf
    beta = math.inf
    # If max play
    if(state[1] == 1):
        value = -math.inf
        next_states = successors(state)
        best_state = next_states[0]
        for x in next_states:
            vnew = minvalue_prune(x, alpha, beta)
            if(value < vnew):
                value = vnew
                best_state = x
            if(vnew >= beta):
                return best_state
            alpha = max(alpha, vnew)
        return best_state
    # Min play
    else:
        value = math.inf
        next_states = successors(state)
        best_state = next_states[0]
        for x in next_states:
            vnew = maxvalue_prune(x, alpha, beta)
            if(value > vnew):   
                value = vnew
                best_state = x
            if(vnew <= alpha):
                return best_state
            beta = min(beta, vnew)
        return best_state


def minimax_value(state):
    # MAX wins
    if(state == ([],1)):
        return 1
    
    # MIN wins
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
