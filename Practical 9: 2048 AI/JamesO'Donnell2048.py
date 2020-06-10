"""
Python 2048 Game : Basic Console Based User Interface For Game Play

Originally written by Phil Rodgers, University of Strathclyde

Altered for CS310 Practical 9 Submission by James O'Donnell

My solution works by "simulating" 100 games each time a move has to
be made. For each simulation, the start move and the final score are
stored in a dictionary, as well as a count of the played games. After
all simulations are complete, the average score is taken for all the
final scores. The score with the given starting move with the highest
average score is selected and used as the actual next move.

Although this solution takes quite a while to reach an end game,
there was no specified time limit on how long the game should be
completed in. However, each move is made within the given time 
limit for each move with a Muir Lab machine as reference.

"""

from py2048_classes import Board, Tile
import time
import copy
import random

def bestMove(possibleMoves, score_dictionary, count_dictionary, highest_score, current_best_move):
    for each_move in possibleMoves:
        if score_dictionary[each_move] / count_dictionary[each_move] > highest_score:
            highest_score = score_dictionary[each_move] / count_dictionary[each_move]
            current_best_move = each_move
    return current_best_move

def generateMove(board, possible_moves):
    
    # Initialising empty dictionaries
    count_dictionary = {}
    score_dictionary = {}
    possibleMoves = possible_moves

    # Populating dictionaries
    for all_moves in possibleMoves:
        score_dictionary[all_moves] = 0
        count_dictionary[all_moves] = 0
    
    # Run the game simulations
    for simulations in range(100):
        move = possibleMoves[random.randint(1,len(possibleMoves)) - 1]
        board_copy = copy.deepcopy(board)
        board_copy.make_move(move)
        board_copy.add_random_tiles(1)
        
        # Using given functions to determine if game is in a terminal state, if not, proceed
        while(not(board_copy.possible_moves() == [] and board_copy.is_board_full())):  
            next_state = board_copy.possible_moves()[random.randint(1,len(board_copy.possible_moves()))-1]
            board_copy.make_move(next_state)
            board_copy.add_random_tiles(1)
            
        # Update the counter and score dictionaries
        count_dictionary[move] += 1
        score_dictionary[move] += board_copy.score
       
    # Initialise current best move and score (Not known and 0)
    current_best_move = possibleMoves[0]
    highest_score = 0
    
    # Return the optimal move
    finalMove = bestMove(possibleMoves,score_dictionary, count_dictionary, highest_score, current_best_move)
    return finalMove


def main():
#allmoves = ['UP','LEFT','DOWN','RIGHT']
    board = Board()
    board.add_random_tiles(2)
    print("main code")

    move_counter = 0
    move = None
    move_result = False
    
    
    overalltime=time.time()
    while True:
        print("Number of successful moves:{}, Last move attempted:{}:, Move status:{}".format(move_counter, move, move_result))
        print(board)
       # print(board.print_metrics())
        if board.possible_moves()==[]:
            if (board.get_max_tile()[0]<2048):
                print("You lost!")
            else:
                print("Congratulations - you won!")
            break
        begin = time.time()
        
###################################### Your code should be inserted below 
###################################### (feel free to define additional functions to determine the next move)
              
        #move = board.possible_moves()[random.randint(0,len(board.possible_moves())-1)]
        #board.make_move(move)
        
        # Returns list of all possible moves
        possible_moves = board.possible_moves()
        
        # Returns the optimal move for the current game state
        next_move = generateMove(board, possible_moves)
        
        # Makes the final move
        board.make_move(next_move)
        
######################################  Do not modify 4 lines below      
######################################
        print("Move time: ", time.time()-begin)
        board.add_random_tiles(1)
        move_counter = move_counter + 1
    print("Average time per move:", (time.time()-overalltime)/move_counter)
    

if __name__ == "__main__":
    main()
