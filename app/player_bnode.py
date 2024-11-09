class PlayerBNode():
    def __init__(self, player):
        self.__player = player
        self.__left = None
        self.__right = None

    @property
    def player(self):
        """

        :return: player
        """
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def left(self):
        """

        :return: left
        """
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        """

        :return: right
        """
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value
