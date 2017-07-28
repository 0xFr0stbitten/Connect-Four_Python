### Connect 4 game on Python
## Class Board
# 

class Board:
    """ a data type for Connect Four board with arbitrary dimensions
    """

    
    def __init__(self, height, width):
        """constructor for Board objects"""
        self.height = height
        self.width = width
        #study the self.slots. Must be [' ']. Doesn't work with ' '.
        self.slots = [[' '] * self.width for row in range(self.height)]



    def __repr__(self):
        """return string representation of Board in Shell""" 
        s = ''
        #add lines betweeen spaces
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        #add horizontal line at the bottom of the board
        s += '-'*((self.width)*2)+'-'
        s += '\n'

        """add column number"""        
        for this_number in range(self.width):
            if this_number>9:
                this_number -= 10
            s += ' ' + str(this_number)
        return s



    def add_checker(self, checker, col):
        """input a checker character X or O in designated column"""
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while self.slots[row][col] == ' ':
            if row == self.height-1:
                self.slots[row][col] = checker

            #move down a row if empty
            elif row < self.height-1:
                if self.slots[row+1][col] == ' ':
                    row += 1
                else:
                    self.slots[row][col] = checker
            else:
                self.slots[row][col] = checker
            


    def reset(self):
        """reset Board to empty spaces"""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '



    def add_checkers(self, columns):
        """ take in a string of column numbers and places alternating
            checkers in columns of the Board, starting with 'X'
        """
        checker = 'X' # start by playing 'X'

        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            #switch checker after each iteration
            if checker == 'X':
                checker = 'O'

            elif checker == 'O':
                checker = 'X'



    def can_add_to(self, col):
        """return True if a checker can be placed in the column col.
           If not, return False.
        """
        if col<0 or col>=self.width:
            return False
        elif self.slots[0][col] != ' ':
            return False
        else:
            return True



    def is_full(self):
        """Return True if board is full. Return False if otherwise"""

        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        #if there is not a single empty space, return True
        return True



    def remove_checker(self, col):
        """remove top checker from column col
           if column is empty, method does nothing
        """
        if self.slots[self.height-1][col] == ' ':
            return
        else:
            row = self.height - 1
            while self.slots[row - 1][col] != ' ':
                row -= 1
            self.slots[row][col] = ' '
            
            



###helper functions

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
             Return true if there is a win.
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True



    def is_vertical_win(self, checker):
        """ Checks for a vertical win for specified checker.
            Return true if there is a win.
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True



    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win for checker
            Move diagonally from top left to bottom right
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True



    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win for checker
            Move diagonally from bottom left to upper right
        """
        for row in range():
            for col in range():
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True



    def is_win_for(self, checker):
        """Accept a paramenter checker and return True if there
           is a winner
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
