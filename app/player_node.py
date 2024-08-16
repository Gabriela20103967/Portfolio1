from player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self.__player = player
        self.__prev = None
        self.__next = None

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def prev(self) -> Player:
        return self.__prev

    @property
    def next(self) -> Player:
        return self.__next

    @prev.setter
    def prev(self, prev_node: Player):
        self.__prev = prev_node

    @next.setter
    def next(self, next_node: Player):
        self.__next = next_node

    @property
    def key(self):
        return self.__player.uid

    def __str__(self) -> str:
        return f"PlayerNode({self.__player}, Previous={self.__prev}, Next={self.__next})"


