import unittest

from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """
        Set up a player instance to be used in tests.
        """
        self.player = Player(uid="1", name="Gabriela", score=10)
        self.player2 = Player(uid="2", name="Tanmay", score=20)
        self.player3 = Player(uid="3", name="John", score=15)
        self.player4 = Player(uid="4", name="Luke", score=10)

    def test_initialization(self):
        """
        Test if the player is initialized with the correct uid and name.
        """
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Gabriela")
        self.assertEqual(self.player.score, 10)

    def test_uid_property(self):
        """
        Test if the uid property of the player.
        """
        self.assertEqual(self.player.uid, "1")

    def test_name_property(self):
        """
        Test if the name property of the player.
        """
        self.assertEqual(self.player.name, "Gabriela")

    def test_str_method(self):
        """
        Test the str method of the player for correct representation.
        """
        self.assertEqual(str(self.player), "Player(uid=1, name=Gabriela, score=10)")

    def test_add_verify_password(self):
        """
        Test that adding and verifying the correct password works.
        """
        self.player.add_password("password1")
        self.assertTrue(self.player.verify_password("password1"))

    def test_add_verify_wrong_password(self):
        """
        Test that verifying an incorrect password fails.
        """
        self.player.add_password("password2")
        self.assertFalse(self.player.verify_password("password3"))

    def test_eq(self):
        """
        Test if the player score is equal to the other player score
        """
        self.assertTrue(self.player.score == self.player4.score)
        self.assertFalse(self.player.score == self.player2.score)

    def test_gt(self):
        """
        Test if the player score is greater than the other player score
        """
        self.assertTrue(self.player2.score > self.player.score)
        self.assertFalse(self.player.score > self.player2.score)

    def test_le(self):
        """
        Test if the player score is less than the other player score
        """
        self.assertTrue(self.player.score < self.player2.score)
        self.assertFalse(self.player2.score < self.player.score)

    def test_sort_descending(self):
        """
        Test the sort_descending method works correctly.
        """
        players = [self.player, self.player2, self.player3, self.player4]
        sorted_players = Player.sort_descending(players)
        self.assertEqual(sorted_players[0].score, self.player2.score)
        self.assertEqual(sorted_players[1].score, self.player3.score)
        self.assertEqual(sorted_players[2].score, self.player4.score)
        self.assertEqual(sorted_players[3].score, self.player.score)


if __name__ == "__main__":
    unittest.main()

