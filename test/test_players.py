import unittest
from Interactions import *
from Moves import *
from Outcomes import *
from Player import *
from MoveList import *

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_setName(self):
        p = HumanPlayer()
        p.setName("Fred flintstone")
        self.assertEqual(p.name, "Fred flintstone")

    def test_botName(self):
        p = BotPlayer()
        p.askForName()
        # Check that bot name starts with "Bot"
        firstChars = p.name[0:3]
        self.assertEqual(firstChars, "Bot")

    def test_HumanAskForMove(self):
        moves = MoveList()
        moveList = moves.getAllMoves()
        p = HumanPlayer()
        p.askForMove(moveList)

