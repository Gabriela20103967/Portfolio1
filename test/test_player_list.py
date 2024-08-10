import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):

    def setUp(self):
        self.pl = PlayerList()

    def test_is_empty(self):
        self.assertTrue(self.pl.is_empty())


if __name__ == '__main__':
    unittest.main()
