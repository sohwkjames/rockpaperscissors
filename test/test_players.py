import unittest
from unittest import patch
from unittest.mock import MagicMock

from Rps import Interactions, Player, MoveList, Outcomes, Moves

class TestPlayer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_setName(self):
        p = Player.HumanPlayer()
        p.setName("Fred flintstone")
        self.assertEqual(p.name, "Fred flintstone")

    def test_generateBotName(self):
        p = Player.BotPlayer()
        result = p.generateBotName()
        firstChars = result[0:3]
        self.assertEqual(firstChars, "Bot")
    
    def test_botName(self):
        p = Player.BotPlayer()
        p.askForName()
        # Check that bot name starts with "Bot"
        firstChars = p.name[0:3]
        self.assertEqual(firstChars, "Bot")

        
    
    # @MagicMock.patch('builtins.input', side_effect=['1'])
    # def test_HumanAskForMove(self):
    #         moves = MoveList.MoveList()
    #         moveList = moves.getAllMoves()
    #         p = Player.HumanPlayer()
    #         p.askForMove(moveList)

