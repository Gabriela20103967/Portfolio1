import unittest

import player as player

from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):

    def setUp(self):
        self.pl = PlayerList()

    def test_is_empty(self):
        self.assertTrue(self.pl.is_empty())

    def test_insert_first(self):
        player = Player("1", "Gabriela")
        self.pl.insert_first(player)
        self.assertFalse(self.pl.is_empty())
        head_node = self.pl._PlayerList__head
        self.assertEqual(head_node.player.uid, "1")
        self.assertEqual(head_node.player.name, "Gabriela")


if __name__ == '__main__':
    unittest.main()
