from player import Player
from player_node import PlayerNode


class PlayerList:
    """
    Attributes:
        __head (PlayerNode): The first node in the list.
        __tail (PlayerNode): The last node in the list.
    """
    def __init__(self) -> None:
        """
        Initializes an empty player list.
        """
        self.__head = None
        self.__tail = None

    @property
    def head(self):
        """
        Gets the head of the list.

        :return:
        PlayerNode: the first node in the list
        """
        return self.__head

    @property
    def tail(self):
        """
        Gets the tail of the list.

        :return:
        PlayerNode: the last node in the list
        """
        return self.__tail

    def is_empty(self):
        """
        Check if the list is empty.

        :return:
        bool: True if the list is empty, and False if is otherwise.
        """
        return self.__head is None

    def insert_first(self, player: Player):
        """
        Insert a player at the beginning of the list.

        Args:
            player (Player): The player to insert.
        """
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def insert_last(self, player: Player):
        """
        Insert a player at the end of the list.

        Args:
            player (Player): The player to insert.
        """
        new_node = PlayerNode(player)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    def delete_head_item(self):
        """
        Delete the first player in the list.
        """
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None

    def delete_tail_item(self):
        """
        Delete the last player in the list.
        """
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None

    def delete_by_key_item(self, id: str):
        """
        Delete a player by their uid.

        Args:
            id (str): The unique identifier of the player to delete.
        """
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

    def display(self, forward=True):
        """
        Display the players in the list.

        Args:
            forward (bool): If is true, display from the head to the tail and
            if is false display from the tail to the head.
        """
        if forward:
            current = self.__head
            while current is not None:
                print(current.player.name)
                current = current.next
        else:
            current = self.__tail
            while current is not None:
                print(current.player.name)
                current = current.prev
        print()

    def __str__(self):
        """
        Return a string representation of the players in the list

        :return:
        str: A string that listing all the players in the list.
        """
        node = []
        current = self.__head
        while current is not None:
            node.append(str(current.player.name))
            current = current.next
        return f"{', '.join(node)}"
