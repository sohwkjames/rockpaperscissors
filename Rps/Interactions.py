from Player import *

class Interactions:
    def __init__(self):
        pass

    def generatePlayers(self, bots=0, n=2):
        result = []
        humanPlayers = n-bots
        while humanPlayers > 0:
            result.append(HumanPlayer())
            humanPlayers -= 1
        while len(result) < n:
            result.append(BotPlayer())
        return result
    
    def askForNames(self, players):    
        for p in players:
            name = p.askForName()
            p.setName(name)
        
    def askForMoves(self, players, moves):
        for p in players:
            move = p.askForMove(moves)
            p.setMove(move)
