#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Fev 6 16:35:42 2020

CS310 Foundations of Artificial Intelligence
Practical 2
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
#print(next_states("MI"))
#print(next_states("MIU"))
#print(next_states("MUI"))
#print(next_states("MIIII"))
#print(next_states("MUUII"))
#print(next_states("MUUUI"))
    
def extendPath(p):   
    
    nextPaths = []
    nextStates = next_states(p[-1])
    
    for x in range(len(nextStates)):
        newPath = p.copy()
        newPath.append(nextStates[x])
        nextPaths.append(newPath)
    return nextPaths

#print("Testing extendPath...\n")
#print(extendPath(["MI", "MII"]))


def breadthFirstSearch (goalString):
    
    agenda = [["MI"]]
    exPCounter = 0
    maxAgen = 0
    
    while (agenda != []):
        currentPath = agenda.pop(0)
        if (currentPath[-1] == goalString):
            print("Length: ", len(currentPath))
            print("extendPath called:",exPCounter,"times.")
            print("Max Agenda Size:", maxAgen)
            return currentPath
        
        elif(exPCounter > 100):
            print("Could not find solution within reasonable amount of time!\n")
            return []
    
        else:
            newPaths = extendPath(currentPath)
            exPCounter += 1
            agenda = agenda + newPaths
            #for i in range(len(newPaths)):
                #agenda.append(newPaths[i])
            
            sizeAgen = len(agenda)
            
            if(sizeAgen > maxAgen):
                maxAgen = sizeAgen
    
#print("\nTesting breadthFirstSearch...\n")
#print(breadthFirstSearch("MIUU"))

    
def depthlimited_dfs(goalString, limit):
    
    agenda = [["MI"]]
    exPCounter = 0
    maxAgen = 0
    
    while (agenda != []):
        currentPath = agenda.pop(0)
        depth = len(currentPath)
        if (currentPath[-1] == goalString):
            print("\nLength: ", len(currentPath))
            print("extendPath called:",exPCounter,"times.")
            print("Max Agenda Size:", maxAgen)
            return currentPath
        
        else:
            if(depth < limit and currentPath != []):
                newPaths = extendPath(currentPath)
                exPCounter += 1
                
                newPaths = newPaths + agenda
                agenda = newPaths.copy()
                depth += 1
                
                sizeAgen = len(agenda)
                if(sizeAgen > maxAgen):
                    maxAgen = sizeAgen
                
    return []

#print("\nTesting depthlimited_dfs...\n")
#print(depthlimited_dfs("MIUIU", 3))


def dfs_iter (goalString):
    
    depth = 3
    callsToDFS = 1
    res = depthlimited_dfs(goalString, depth)
    
    while(res == [] or res == None) and (depth < 30):
        res = depthlimited_dfs(goalString, depth)
        callsToDFS +=1
        depth +=1
    print("Calls to DFS:", callsToDFS)
    return res

    
print(breadthFirstSearch("MUIU"))
print(dfs_iter("MUIU"))








