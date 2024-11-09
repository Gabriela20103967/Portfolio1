class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        """
        Getter for the player
        :return: player
        """
        return self.__player

    @player.setter
    def player(self, value):
        """
        Setter for the player
        :param value: The new player object
        """
        self.__player = value

    @property
    def left(self):
        """
        Getter for the left child
        :return: left child
        """
        return self.__left

    @left.setter
    def left(self, value):
        """
        Setter for the left child
        :param value: The new left child node
        """
        self.__left = value

    @property
    def right(self):
        """
        Getter for the right child
        :return: right child
        """
        return self.__right

    @right.setter
    def right(self, value):
        """
        Setter for the right child
        :param value: The new right child node
        """
        self.__right = value
