### Connect Four Game on Python
## Class 2 - Player
#

from BoardClass import Board

class Player:
    """ A class that represents a player in the game
    """

    def __init__(self, checker):
        """ construct a new Player object
            attributes are checker and num_moves
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0



    def __repr__(self):
        """ Return a string represent a Player object
            The string should indicate which checker is being used
        """
        return 'Player ' + self.checker



    def opponent_checker(self):
        """ Return a one-character string
            Represents checker of Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'



    def next_move(self, board):
        """ Return column where player wants to make the move
            Ask user to enter column number
            This method does not take into consideration if the column
            is full
        """
        col = int(input("Enter a column: "))

        #Ask again if move isn't valid
        if board.can_add_to(col) == False:
            print('Try again!')
            return self.next_move(board)

        elif board.can_add_to(col) == True:
            self.num_moves += 1
            return col
                
