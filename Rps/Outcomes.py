class Outcomes:
    def __init__(self):
        self.allOutcomes = {}
        pass

    def matchUp(self, move1, move2):
        # takes 2 move objects, returns the winning move object
        if move1.matchUps['draw'] == move2.id:
            return None
        elif move1.matchUps['win'] == move2.id:
            return move1
        elif move1.matchUps['lose'] == move2.id:
            return move2
        else:
            return None
    
    def getWinner(self, player1, player2):
        p1Move = player1.move
        p2Move = player2.move
        result = self.matchUp(p1Move, p2Move)
        if result == None:
            return None
        if p1Move == result:
            return player1
        if p2Move == result:
            return player2
        else:
            return None

    def getResultString(self, player1, player2):
        message = "{} has played {}. {} has played {}. ".format(player1.name, player1.move, player2.name, player2.move)
        winner = self.getWinner(player1, player2)
        if winner == None:
            message += "It is a draw game!"
            return message
        else:
            message += "Winner is {}".format(winner.name)
            return message
        


    