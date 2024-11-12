import unittest
from player import Player
from player_bst import PlayerBST


class TestPlayerBST(unittest.TestCase):

    def setUp(self):
        '''Sets up the test variables. Creates instances of Player objects to be used in the tests.'''
        self.bst = PlayerBST()
        self.player = Player(uid="1", name="Gabriela", score=12)
        self.player2 = Player(uid="2", name="Tanmay", score=15)
        self.player3 = Player(uid="3", name="John", score=4)
        self.player4 = Player(uid="4", name="Luke", score=50)

    def test_insert(self):
        '''Tests the insert method of the PlayerBST class'''
        self.bst.insert(self.player)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)

        self.assertEqual(self.bst.root.player.name, "Gabriela")
        self.assertEqual(self.bst.root.left.player.name, "Tanmay")
        self.assertEqual(self.bst.root.right.player.name, "John")
        self.assertEqual(self.bst.root.left.right.player.name, "Luke")

    def test_search_not_found(self):
        """
        Tests the search function for a player name that does not exist in the BST.
        :return:
        """
        self.bst.insert(self.player)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)

        no_player = self.bst.search("Maria")
        self.assertIsNone(no_player)

    def test_search_found(self):
        """
        Tests the search function for a player name that exists in the BST.
        :return:
        """
        self.bst.insert(self.player)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)

        found_player = self.bst.search("Gabriela")
        self.assertIsNotNone(found_player)
        self.assertEqual(found_player.name, "Gabriela")



if __name__ == '__main__':
    unittest.main()





