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

    def delete_head_item(self):
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

    def delete_tail_item(self):
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

    def delete_by_key_item(self, id: str):
        current = self.__head

        while current is not None:
            if current.player.uid == id:
                if current == self.__head:
                    self.delete_head_item()
                    return

                elif current == self.__tail:
                    self.delete_tail_item()
                    return

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

            current = current.next


    def __str__(self):
        node = []
        current = self.__head
        while current is not None:
            node.append(str(current.player.name))
            current = current.next
        return f"{', '.join(node)}"


