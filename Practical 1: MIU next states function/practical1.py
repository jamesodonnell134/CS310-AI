#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:20:42 2020

CS310 Foundations of Artificial Intelligence
Tutorial 1: MIU System

@author: jamesodonnell
"""

def next_states(s):
    output = []
    
    # Rule 1: xI -> xIU
    if (s[-1] == 'I'):
        output.append(s + 'U')
        
    # Rule 2: Mx -> Mxx
    if (s[0] == 'M'):
        output.append(s + "" + s[1:])
            
    # Rule 3: xIIIy -> xUy
    for x in range (len(s[1:-1])):
        if(s[x:(x+3)] == 'III'):
            output.append(s[:x] + "U" + s[(x+3):])

    # Rule 4: xUUy -> xy
    for x in range (len(s[1:-1])):
        if(s[x:(x+2)] == 'UU'):
            output.append(s[:x] + "" + s[(x+2):])
        
    finalOutput = []
    
    # Removing duplicates
    for x in range(len(output)):
        if(output[x] not in finalOutput):
            finalOutput.append(output[x])
    return finalOutput

# Tests
print(next_states("MI"))
print(next_states("MIU"))
print(next_states("MUI"))
print(next_states("MIIII"))
print(next_states("MUUII"))
print(next_states("MUUUI"))






