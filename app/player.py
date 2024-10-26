from argon2 import PasswordHasher

class Player:
    """
    A class which represent a player

    Attributes:
        uid (str): The unique identifier for the player.
        name (str): The name of the player.
        score (int): The score of the player.
    """
    def __init__(self, uid: str, name: str, score: int) -> None:
        """
        Initializes a player instance

        Args:
            uid (str): The unique identifier for the player.
            name (str): The name of the player.
            score (int): The score of the player
        """
        self.__uid = uid
        self.__name = name
        self.__score = score

    @property
    def uid(self) -> str:
        """
        Gets the uid of the player.

        :return:
        str: The unique identifier of the player
        """
        return self.__uid

    @property
    def name(self) -> str:
        """
        Gets the name of the player

        :return:
        str: The name of the player
        """
        return self.__name

    @property
    def score(self) -> int:
        """
        Gets the score of the player

        :return:
        int: The score of the player.
        """
        return self.__score

    @score.setter
    def score(self, new_score: int):
        """
        Sets a new score for the player

        Args:
            new_score (int): Set the new score for the player.
        Raises:
            ValueError: if the new score is negative
        """
        if new_score < 0:
            raise ValueError("Score must be a positive number")
        self.__score = new_score

    def add_password(self, password: str):
        """
        Hashes and store the player's password.

        Args:
            password (str): The password to be hashed and store.
        """
        ph = PasswordHasher()
        self.__hashed_password = ph.hash(password)

    def verify_password(self, password: str):
        """
        Verify the provide password against the stored hashed password.

        Args:
            password (str): The password to verify
        :return:
        bool: True if the password match with the store hash, and false otherwise.

        """
        ph = PasswordHasher()
        try:
            return ph.verify(self.__hashed_password, password)
        except:
            return False

    def __eq__(self, other):
        """
        Check if the score is equal to the other score

        Args:
            other (Player): The other player score
        :return:
        bool: True if the score of the player is equal, false otherwise
        """
        return self.__score == other.score

    def __gt__(self, other):
        """
        Check if the score is greater to the other score

        Args:
            other (Player): The other player score

        :return:
        bool: True if the scores of the player is greater, false otherwise
        """
        return self.__score > other.score

    def __le__(self, other):
        """
        Check if the score is less to the other score

        Args:
            other (Player): The other player score
        :return:
        bool: True if the score of the player is less, false otherwise
        """
        return self.__score < other.score

    @staticmethod
    def sort_descending(players: list):
        """
        Sort a list of the players scores in descending order using bubble sort algorithm.

        Args:
            players (list): A list of player instances to be sorted.
        :return:
        list: A list of player sorted in descending order by score.
        """
        n = len(players)
        for i in range(n):
            for j in range(0, n-i-1):
                if players[j].score < players[j+1].score:
                    players[j], players[j+1] = players[j+1], players[j]
        return players

    def __str__(self):
        """
        Return a string representation of the player.

        :return:
        str: a string that describe the player
        """
        return f"Player(uid={self.__uid}, name={self.__name}, score={self.__score})"


def main():
    player1 = Player(uid="1", name="Gabriela", score=10)
    player2 = Player(uid="2", name="Tanmay", score=20)
    player3 = Player(uid="3", name="John", score=15)
    player4 = Player(uid="4", name="Luke", score=36)

    print("Player:")
    print(str(player1))
    print(str(player2))
    print(str(player3))
    print(str(player4))

    players = [player1, player2, player3, player4]
    print(f"Unsorted list :")
    for player in players:
        print(player)

    sorted_list = Player.sort_descending(players)
    print(f"Sorted list :")
    for player in sorted_list:
        print(player)


if __name__ == "__main__":
    main()

