from player import Player


class PlayerNode:
    """
    Args:
        __player (Player): The player associated with this node.
        __prev (Player): The previous node in the list.
        __next (Player): The next node in the list.
    """
    def __init__(self, player: Player) -> None:
        """
        Initiliazes a player node with the given player.

        Args:
             player (Player): The player to associated with this node.
        """
        self.__player = player
        self.__prev = None
        self.__next = None

    @property
    def player(self) -> Player:
        """
        Gets the player associated with this node.

        :return:
        Player: The player associated with this node.
        """
        return self.__player

    @property
    def prev(self) -> Player:
        """
        Gets the previous node in the list.

        :return:
        PlayerNode: The previous node in the list.
        """
        return self.__prev

    @property
    def next(self) -> Player:
        """
        Gets the next node in the list.

        :return:
        PlayerNode: The next node in the list.
        """
        return self.__next

    @prev.setter
    def prev(self, prev_node: Player):
        """
        Set the previous node in the list

        Args:
            prev_node (PlayerNode): The node to set as the previous node.
        """
        self.__prev = prev_node

    @next.setter
    def next(self, next_node: Player):
        """
        Set the next node in the list.

        Args:
            next_node (PlayerNode): The node to set as the next node.
        """
        self.__next = next_node

    @property
    def key(self):
        """
        Get the uid of the player with this node.

        :return:
        str: The uid of the player.
        """
        return self.__player.uid

    def __str__(self) -> str:
        """
        Return a string representation of the PlayerNode.

        :return:
        str: A string describing the player and the previous and next nodes.
        """
        return f"PlayerNode({self.__player}, Previous={self.__prev}, Next={self.__next})"


