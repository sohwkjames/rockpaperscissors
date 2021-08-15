import unittest

class TestOutcomes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v1 = 9
        cls.v2 = 20


    def test_Add(self):
        print(self.v1)
        print(self.v2)
        self.v1 = self.v1*2
        print(self.v1)
        self.assertEqual(self.v1+self.v2, 29)

    def test_secondTest(self):
        print("Debug!")
        print(self.v1) # should be 9
        print(self.v2)