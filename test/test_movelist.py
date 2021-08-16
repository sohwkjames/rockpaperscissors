import unittest
from Interactions import *
from Moves import *
from Outcomes import *
from Player import *
from MoveList import *


class TestMovelist(unittest.TestCase):

    def test_getAllMoves(self):
        movelist = MoveList()
        result = movelist.getAllMoves()
        expected = [Rock(), Paper(), Scissors()]
        self.assertIsInstance(result[0], Rock)
        self.assertIsInstance(result[1], Paper)
        self.assertIsInstance(result[2], Scissors)
