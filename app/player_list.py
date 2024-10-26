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
            if current.key == id:
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

    def to_list(self):
        """ Converts the linked list of players into a Python list."""
        players = []
        current = self.__head
        while current:
            players.append(current.player)
            current = current.next
        return players

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
                print(f"UID: {current.player.uid}, Name: {current.player.name}")
                current = current.next
        else:
            current = self.__tail
            while current is not None:
                print(f"UID: {current.player.uid}, Name: {current.player.name}")
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
            prev_uid = current.prev.player.uid if current.prev else "None"
            next_uid = current.next.player.uid if current.next else "None"
            node.append(f"Prev: {prev_uid}, UID: {current.player.uid}, Name: {current.player.name}, Next: {next_uid}")
            current = current.next
        return f"{' -> '.join(node)}"


def main():
    player1 = Player(uid="01", name="Gabriela")
    player2 = Player(uid="02", name="Tanmay")
    player3 = Player(uid="03", name="Maria")
    player_list = PlayerList()
    player_list.insert_first(player1)
    player_list.insert_last(player2)
    player_list.insert_last(player3)

    print("Player from head to tail:")
    player_list.display(forward=True)

    print("Player from tail to head:")
    player_list.display(forward=False)

    print("Deleting Player")
    player_list.delete_by_key_item("02")
    player_list.display(forward=True)

    print("The double linked list")
    print(player_list)


if __name__ == "__main__":
    main()
