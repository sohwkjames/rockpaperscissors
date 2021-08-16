import unittest
from Rps import Interactions, Player, MoveList, Outcomes, Moves

class TestMovelist(unittest.TestCase):

    def test_getAllMoves(self):
        movelist = MoveList.MoveList()
        result = movelist.getAllMoves()
        expected = [Moves.Rock(), Moves.Paper(), Moves.Scissors()]
        self.assertIsInstance(result[0], Moves.Rock)
        self.assertIsInstance(result[1], Moves.Paper)
        self.assertIsInstance(result[2], Moves.Scissors)
