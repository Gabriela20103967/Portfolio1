from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    def is_empty(self):
        return self.__head is None

    def insert_first(self, player: Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def insert_last(self, player:Player):
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    def __str__(self):
        node = []
        current = self.__head
        while current is not None:
            node.append(str(current))
            current = current.next
        return "->".join(node)


def main():
    player1 = Player("1", "Gabriela")
    player2 = Player("2", "Tanmay")
    pl1 = PlayerList()
    pl1.insert_first(player1)
    pl1.insert_last(player2)
    print("Player List:")
    print(pl1)


if __name__ == "__main__":
    main()
