### Put the Game Together
## Connect Four Game
#

from AI_Player import *       
        
    
print(" To play a game of connect four with two players, enter 'Play_C4_2P()'. To \
play \n with AI, enter 'Play_C4_AI()'.")

def Play_C4_2P():
    """Play the game Connect Four!"""
    print(" Enter '2P' to play with two players or enter 'AIP' to play with AI.")
    p1 = Player('X')
    p2 = Player('O')
    return connect_four(p1, p2)



def Play_C4_AI():
    """Play C4 with AI"""
    p1 = Player('X')
    choice = input("Pick your tiebreaking strategy. Pick 'LEFT', 'RIGHT', or 'RANDOM':")
    lookahd = int(input("Pick a number greater than or equal to 0 for AI to look ahead:"))
    if choice not in 'LEFT,RIGHT,RANDOM' or lookahd <0:
        print("You have entered invalid choices. Please try again.")
        return Play_C4_AI()
    p2 = AIPlayer('O', choice, lookahd)
    return connect_four(p1, p2)
