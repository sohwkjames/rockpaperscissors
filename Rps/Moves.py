class Move:
    def __init__(self):
        # self.matchUps is some dict in the shape: {'win': 2, 'lose':1, 'draw':3} 
        # this move wins against move id 2, lose against move id 1, draw against move id 3
        self.name
        self.id
        self.matchUps = {}
        
class Rock(Move):
    def __init__(self):
        self.name="Rock"
        self.id = 1
        self.matchUps = {'win': 3, 'lose': 2, 'draw':1}
        
class Paper(Move):
    def __init__(self):
        self.name="Paper"
        self.id = 2
        self.matchUps = {'win': 1, 'lose': 3, 'draw':2}

class Scissors(Move):
    def __init__(self):
        self.name="Scissors"
        self.id = 3
        self.matchUps = {'win': 2, 'lose': 1, 'draw':3}