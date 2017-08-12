### Connect Four Game on Python
## Class three - Playing the game; class - RandomPlayer
#

from BoardClass import Board
from PlayerClass import Player
import random

#function process_move(player, board)

def process_move(player, board):
    """Take parameters Player and Board
       Process a single move by Player on Board
    """
    print(player.__repr__() + "'s turn")
    if player.__repr__() == 'Player X' or 'Player X' in player.__repr__():
        checker = 'X'
    elif player.__repr__() == 'Player O' or 'Player O' in player.__repr__():
        checker = 'O'
    move = player.next_move(board)
    board.add_checker(checker, move)
    print('')
    print(board) 
    if board.is_win_for(checker) == True:
        number_moves = player.num_moves
        string_moves = str(number_moves)
        print(player.__repr__(), "wins in", number_moves, "moves.")
        print("Congratulations!")
        return True
    elif board.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

#subclass RandomPlayer

class RandomPlayer(Player):
    """ Class for unintelligent computer player that randomly plays
    """
    def __init__(self, checker):
        """ Construct RandomPlayer object
            Copy all attributes from Player class
        """
        super().__init__(checker)

    def __repr__(self):
        """ Copy method from Player class
        """
        super().__repr__()



    def next_move(self, board):
        """ Override next_move method from Player class
            Choose next move randomly from columns that are not full
        """
        columns = []
        for x in range(board.width):
            if board.can_add_to(x) == True:
                x = str(x)
                columns =+ [x]

        self.num_moves += 1
        return int(random.choice(columns))


    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)

    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
