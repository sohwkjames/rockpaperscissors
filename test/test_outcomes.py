import unittest
from Rps import Interactions, Player, MoveList, Outcomes, Moves

class TestOutcomes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This runs before each test is run within this class.
        cls.p1 = Player.Player()
        cls.p1.setName("Alice")
        cls.p1.move = Moves.Rock()
        
        cls.p2 = Player.Player()
        cls.p2.setName("Bob")
        cls.p2.move = Moves.Paper()

        cls.outcomes = Outcomes.Outcomes()

    def test_matchUp(self):

        move1 = Moves.Rock()
        move2 = Moves.Paper()
        result = self.outcomes.matchUp(move1, move2)
        self.assertEqual(result, move2)

        move2 = Moves.Rock()
        result = self.outcomes.matchUp(move1, move2)
        self.assertEqual(result, None, "should return None if even matchUp")
    
    def test_getWinner(self):

        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, self.p2, "paper should beat rock")

        self.p2.move = Moves.Scissors()
        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, self.p1, "rock should beat scissors")

        self.p2.move = Moves.Rock()
        result = self.outcomes.getWinner(self.p1, self.p2) 
        self.assertEqual(result, None, "draw game should return None")

    def test_getResultString(self):

        result = self.outcomes.getResultString(self.p1, self.p2)
        expected = "Alice has played rock. Bob has played paper. Winner is Bob!"
        self.assertEqual(result, expected)

        self.p2.currentMove = Moves.Rock()
        result = self.outcomes.getResultString(self.p1, self.p2)
        expected = "Alice has played rock. Bob has played paper. It is a draw game!"
        