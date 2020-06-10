#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:05:43 2020

CS310 Foundations of Artificial Intelligence
Practical 3
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
    
    f = open("MUI-OUTPUT-BFS.txt", "w")

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
            f.write(str(agenda));
            f.write("\n\n");
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

    
#print(breadthFirstSearch("MUIU"))
#print(dfs_iter("MUIU"))


#############################################
# Practical 3 starts here
#############################################


def bfsDict (goalString):
    
    # For testing purposes
    f = open("bfsDict-OUTPUT.txt", "w")
    
    dictionary = {}
    agenda = ["MI"]
    output = []
    counter = 0
    
    while(counter < 123):
        current = agenda.pop(0)
        if(current == goalString):
            print("Extensions: " , counter)
            output.append(current)
            while(current != "MI"):
                current = dictionary[current]
                output.insert(0, current)
            return output
        else:
            states = next_states(current)
            for i in range(len(states)):
                if states[i] not in dictionary:
                    dictionary[states[i]] = current
    
                    # For testing purposes
                    f.write(str(dictionary));
                    f.write("\n\n");
            agenda = agenda + states
            counter += 1
           
    print("Extensions exceeded! Extensions: ", counter)
    return []
    f.close()
    
#print(bfsDict("MIUUI"))


def estimateSteps(current, goalString):
    if (current == goalString):
        return 0
    else:
        return 1


def a_starSearch(goal_str):
    unvisited = ["MI"]
    path_map = {"MI": "M"}

    cheapest = {"MI": 0}
    est_score = {"MI": estimateSteps("MI")}
    
    while (unvisited):
        current_node = min(est_score, key=est_score.get)
        
        if current_node == goal_str:
            #return path_finder(path_map, goal_str)
    
            unvisited.remove(current_node)
            neighbours = next_states(current_node)
       
        for x in range(len(neighbours)):
            guess = cheapest[current_node] + estimateSteps(current_node, neighbours[x])
            
            if guess < cheapest[neighbours[x]]:
                path_map[neighbours[x]] = current_node
                cheapest[neighbours[x]] = guess
                est_score[neighbours[x]] = cheapest[neighbours[x]] + 0
                
                if neighbours[x] not in unvisited:
                    unvisited.append(neighbours[x])
    
    return []    




    
    
    
    
    
    
    
    
    
    
    
    
    














