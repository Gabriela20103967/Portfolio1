import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """
        Set up a player instance to be used in tests.
        """
        self.player = Player(uid="1", name="Gabriela")

    def test_initialization(self):
        """
        Test if the player is initialized with the correct uid and name.
        """
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Gabriela")

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
        self.assertEqual(str(self.player), "Player(uid=1, name=Gabriela)")

    def test_add_verify_password(self):
        self.player.add_password("password12")
        self.assertTrue(self.player.verify_password("password12"))

    def test_add_verify_wrong_password(self):
        self.player.add_password("password34")
        self.assertFalse(self.player.verify_password("password3"))


if __name__ == '__main__':
    unittest.main()
