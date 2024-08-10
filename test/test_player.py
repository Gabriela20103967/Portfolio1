import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(uid="1", name="Gabriela")

    def test_initialization(self):
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Gabriela")

    def test_uid_property(self):
        self.assertEqual(self.player.uid, "1")

    def test_name_property(self):
        self.assertEqual(self.player.name, "Gabriela")

    def test_str_method(self):
        self.assertEqual(str(self.player), "Player(uid=1, name=Gabriela)")

