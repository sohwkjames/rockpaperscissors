import unittest
from Rps.Interactions import *
from Rps.Moves import *
from Rps.Outcomes import *
from Rps.Player import *

class TestOutcomes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This runs before each test is run within this class.
        cls.p1 = Player()
        cls.p1.setName("Alice")
        cls.p1.currentMove = Rock()
        
        cls.p2 = Player()
        cls.p2.setName("Bob")
        cls.p2.currentMove = Paper()

        cls.outcomes = Outcomes()

    def test_matchUp(self):

        move1 = Rock()
        move2 = Paper()
        result = self.outcomes.matchUp(move1, move2)
        self.assertEqual(result, move2)

        move2 = Rock()
        result = self.outcomes.matchUp(move1, move2)
        self.assertEqual(result, None, "should return None if even matchUp")
    
    def test_getWinner(self):

        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, self.p2, "paper should beat rock")

        self.p2.currentMove = Scissors()
        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, self.p1, "paper should beat rock")

        self.p2.currentMove = Rock()
        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, None, "draw game should return None")

    def test_getResultString(self):

        result = self.outcomes.getResultString(self.p1, self.p2)
        expected = "Alice has played rock. Bob has played paper. Winner is Bob!"
        self.assertEqual(result, expected)

        self.p2.currentMove = Rock()
        result = outcomes.getResultString(p1, p2)
        expected = "Alice has played rock. Bob has played paper. It is a draw game!"
        

    

