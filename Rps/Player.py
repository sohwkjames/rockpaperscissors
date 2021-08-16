import random

class Player:
    def __init__(self):
        # move is a Move object.
        self.name = ""
        self.move = 0
    
    def askForName(self):
        pass

    def setName(self, name):
        self.name = name

    def askForMove(self, moves):
        pass

    def setMove(self, move):
        self.move = move
    
class HumanPlayer(Player):
    def askForName(self):
        result = input("Please enter a name for this player \n")
        return result
    
    def askForMove(self,moves):
        print("Please choose a move")
        i = 0
        for move in moves:
            print ("{}: {}".format(i, move.name))
            i += 1
        response = int(input())
        return moves[response]

class BotPlayer(Player):
    def askForName(self):
        return self.generateBotName()

    def askForMove(self, moves):
        response = random.randint(0, len(moves)-1)
        return moves[response]

    def generateBotName(self):
        return "Bot" + str(random.randint(1,100))

