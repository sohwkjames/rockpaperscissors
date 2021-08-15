import unittest
from Rps.Interactions import *
from Rps.Moves import *
from Rps.Outcomes import *
from Rps.Player import *

class TestInteractions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This runs before each test is run within this class.
        pass

    def test_generatePlayers(self):
        interactions = Interactions()
        result = interactions.generatePlayers(bots=1, n=2) # expect 2 Players, 0 Bots
        self.assertIsInstance(result[0], HumanPlayer)
        self.assertIsInstance(result[0], BotPlayer)

        result = interactions.generatePlayers(bots=0, n=2) # expect 2 Players, 0 Bots
        self.assertIsInstance(result[0], BotPlayer)
        self.assertIsInstance(result[0], BotPlayer)

        