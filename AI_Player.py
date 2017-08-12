### AI Player
## Connect Four Game
#

import random
from RandomPlayer import *

class AIPlayer(Player):
    """ Create a subclass AIPlayer of Player
        This is an AI player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ Copy object method from Player class
            Insert two new attributes tiebreak and lookahead
            Tiebreak breaks ties and lookahead stores how many moves the
            player looked ahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = int(lookahead)



    def __repr__(self):
        """ Return string representing AIPlayer object
            Override __repr__ method inherited from Player
            Indicate the checker used and teibreaking and lookahead strategy
        """
        super().__repr__()
        return super().__repr__() +' ('+self.tiebreak+', '+str(self.lookahead)+')'



    def max_score_column(self, scores):
        """ Take list scores containing score for each column
            Return index of column with highest column
            If columns are tied, use tiebreaking strategy
        """
        max_scores = []
        maximum = max(scores)
        for x in range(len(scores)):
            if scores[x] == maximum:
                max_scores += [x]

        if self.tiebreak == 'LEFT':
            return max_scores[0]
        elif self.tiebreak == 'RIGHT':
            return max_scores[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_scores)



    def scores_for(self, board):
        """ Take Board object and determine AIPlayer's scores for columns
            Each column should be assigned one of the four possible scores
            Return a list containing a score for each column
        """
        other_checker = self.opponent_checker()
        scores = []
        number_columns = board.width
        for x in range(board.width):
            scores += [50]

        for y in range(len(scores)):
            if board.can_add_to(y) == False:
                scores[y] = -1
            elif board.is_win_for(self.checker):
                scores[y] = 100
            elif board.is_win_for(other_checker):
                scores[y] = 0
            elif self.lookahead == 0:
                scores[y] = 50
            else:
                board.add_checker(self.checker, y)
                opponent = AIPlayer(other_checker, self.tiebreak, self.lookahead-1)
                potential_scores = opponent.scores_for(board)
                board.remove_checker(y)

                if max(potential_scores) == 0:
                    scores[y] = 100
                elif max(potential_scores) == 50:
                    scores[y] = 50
                elif max(potential_scores) == 100:
                    scores[y] = 0
            return scores



    def next_move(self, board):
        """ Override next_move method from Player
            Return AIPlayer's best move
        """

        self.num_moves = self.num_moves + 1
        API_moves = self.scores_for(board)
        best_move = self.max_score_column(API_moves)
        return best_move
