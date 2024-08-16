import unittest

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
        head_node = self.pl.head
        self.assertEqual(head_node.player.uid, "1")
        self.assertEqual(head_node.player.name, "Gabriela")

    def test_insert_last(self):
        player = Player("2", "Tanmay")
        self.pl.insert_last(player)
        self.assertFalse(self.pl.is_empty())
        tail_node = self.pl.tail
        self.assertEqual(tail_node.player.uid, "2")
        self.assertEqual(tail_node.player.name, "Tanmay")


if __name__ == '__main__':
    unittest.main()
