import unittest

from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):

    def setUp(self):
        """
        Set up the Playerlist and player instance for use in test.
        """
        self.playerlist = PlayerList()
        self.player = Player(uid="1", name="Gabriela")
        self.player2 = Player(uid="2", name="Tanmay")
        self.player3 = Player(uid="3", name="Maria")

    def test_is_empty(self):
        """
        Test that a new Playerlist is initially empty.
        """
        self.assertTrue(self.playerlist.is_empty)

    def test_insert_first(self):
        """
        Test inserting players at the head of the list.
        """
        self.playerlist.insert_first(self.player)
        self.playerlist.insert_first(self.player2)
        self.assertEqual(self.playerlist.head.player, self.player2)

    def test_insert_last(self):
        """
        Test inserting players at the tail of the list.
        """
        self.playerlist.insert_last(self.player)
        self.playerlist.insert_last(self.player2)
        self.assertEqual(self.playerlist.tail.player, self.player2)

    def test_delete_head_item(self):
        """
        Test deleting the head item from the list.
        """
        self.playerlist.insert_last(self.player)
        self.playerlist.insert_last(self.player2)
        self.playerlist.delete_head_item()
        self.assertEqual(self.playerlist.head.player, self.player2)

    def test_delete_tail_item(self):
        """
        Test deleting the tail from the list.
        """
        self.playerlist.insert_last(self.player)
        self.playerlist.insert_last(self.player3)
        self.playerlist.delete_tail_item()
        self.assertEqual(self.playerlist.tail.player, self.player)

    def test_delete_by_key(self):
        """
        Test deleting a player by uid from the list.
        """
        self.playerlist.insert_first(self.player)
        self.playerlist.insert_last(self.player2)
        self.playerlist.insert_last(self.player3)
        self.playerlist.delete_by_key_item("2")
        self.assertEqual(str(self.playerlist),  "Gabriela, Maria")


if __name__ == '__main__':
    unittest.main()
