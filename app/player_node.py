from player import Player


class PlayerNode:
    def __init__(self, player: Player) -> None:
        self.__player = player
        self.__next = None
        self.__prev = None

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def next(self) -> Player:
        return self.__next

    @next.setter
    def next(self, next_node: Player):
        self.__next = next_node

    @property
    def prev(self) -> Player:
        return self.__prev

    @prev.setter
    def prev(self, prev_node: Player):
        self.__prev = prev_node


    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f"PlayerNode(player={self.__player}, previous={self.__prev}, next={self.__next})"


def main():
    player = Player("1", "Gabriela")
    plnode = PlayerNode(player)
    print(str(player))
    print(str(plnode))


if __name__ == "__main__":
    main()

