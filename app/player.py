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
        """
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
    def sort_descending(scores: list):
        """
        Sort a list of the players scores in descending order using bubble sort algorithm.

        Args:
            scores (list): A list of player scores to be sorted.
        :return:
        list: A list of scores sorted in descending order.
        """
        n = len(scores)
        for i in range(n):
            for j in range(0, n-i-1):
                if scores[j] < scores[j+1]:
                    scores[j], scores[j+1] = scores[j+1], scores[j]
        return scores

    def __str__(self):
        """
        Return a string representation of the player.

        :return:
        str: a string that describe the player
        """
        return f"Player(uid={self.__uid}, name={self.__name}, score={self.__score})"


def main():
    scores = [90, 20, 15, 36]
    print(f"Unsorted list: {scores}")

    sorted_scores = Player.sort_descending(scores)
    print(f"Sorted list: {sorted_scores}")


if __name__ == "__main__":
    main()


