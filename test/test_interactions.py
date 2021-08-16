import unittest
from Rps import Interactions, Player, MoveList, Outcomes, Moves


class TestInteractions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This runs before each test is run within this class.
        pass

    def test_generatePlayers(self):
        interactions = Interactions.Interactions()
        result = interactions.generatePlayers(bots=1, n=2) # expect 2 Players, 0 Bots
        self.assertIsInstance(result[0], Player.HumanPlayer)
        self.assertIsInstance(result[1], Player.BotPlayer)

        result = interactions.generatePlayers(bots=2, n=2) # expect 2 Players, 0 Bots
        self.assertIsInstance(result[0], Player.BotPlayer)
        self.assertIsInstance(result[1], Player.BotPlayer)
