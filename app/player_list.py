from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def insert_first(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
