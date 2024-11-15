from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    """
    This class implement a Binary search Tree to store and manage each node in the
    """
    def __init__(self):
        """
        Initialize an empty BST with no root node
        """
        self._root = None

    @property
    def root(self):
        """Returns the root node of the tree."""
        return self._root

    def insert(self, player: Player):
        """
        Adds a new player node to the BST based on the player's name.

        Args:
            player (Player): The Player object to add.
        """
        new_node = PlayerBNode(player)
        new_node.key = player.name
        new_node.value = player

        if self._root is None:
            print(f"this is the root player: {new_node.key}")
            self._root = new_node
        else:
            current_node = self._root
            while True:
                parent = current_node
                if player.name == current_node.player.name:
                    print(f"Duplicate name: {player.name}")
                    return

                if player.name < current_node.player.name:
                    current_node = current_node.left
                    if current_node is None:
                        parent.left = new_node
                        return
                elif player.name > current_node.player.name:
                    current_node = current_node.right
                    if current_node is None:
                        parent.right = new_node
                        return

    def search(self, name):
        """
        Searches for a player by name in the BST.

        Args:
            name (str): The name of the player to find.

        Returns:
            Player: The player object is found, or None if not found.
        """
        return self.prepare_search(self._root, name)

    def prepare_search(self, current, name):
        """
        Helps to the search method to navigate through the BST to find a player by name.

        Args:
            current (PlayerBNode): The node to start searching from.
            name (str): The name of the player to find.
        Returns:
            Player: The player object if found, or None if not found.
        """
        while current.player.name != name:
            if name < current.player.name:
                current = current.left
            elif name > current.player.name:
                current = current.right

            if current is None:
                print(f"{name} is not found!!")
                return None

        print(f"{name} is found!")
        return current.player

    def traverse(self):
        """
        Performs an in-order traversal of the BST, returning all nodes in sorted order.

        Returns:
            list: A list of PlayerBNode objects sorted by player name.
        """
        nodes = []
        print("In-order traversal: ")
        self.in_order_helper(self._root, nodes)
        return nodes

    def in_order_helper(self, node, nodes):
        """
        Recursively visits each node in-order (left, root, right) and collects them in a list.

        Args:
            node(PlayerBNode): The current node being visited.
            nodes(list): The list to collect nodes in sorted order.

        """
        if node is not None:
            self.in_order_helper(node.left, nodes)
            nodes.append(node)
            print(str(node.player))
            self.in_order_helper(node.right, nodes)

    def balanced_tree(self, nodes, start, end):
        """
        Builds a balanced BST from a sorted list of nodes.

        Args:
            nodes(list): The sorted list of PlayerBNode objects.
            start(int): The starting index of the list.
            end(int): The ending index of the list.

        Returns:
            PlayerBNode: The root of the balanced BST
        """
        if start > end:
            return None
        mid = (start + end) // 2
        self._root = PlayerBNode(nodes[mid])
        self._root.left = self.balanced_tree(nodes, start, mid -1)
        self._root.right = self.balanced_tree(nodes, mid + 1, end)
        return self._root

    def balance_bst(self):
        """
        Balances the current BST to improve search efficiency.

        Returns:
            PlayerBNode: The new root of the balanced BST.
        """
        nodes = []
        self.in_order_helper(self._root, nodes)
        return self.balanced_tree(nodes, 0, len(nodes) -1)

def main():
    tree = PlayerBST()

    player = Player("1", "Gabriela", 12)
    player2 = Player("2", "Tanmay", 15)
    player3 = Player("3", "John", 4)
    player4 = Player("4", "Luke", 50)
    player5 = Player("5", "Nicolas", 15)
    player6 = Player("6", "Sven", 15)

    tree.insert(player)
    tree.insert(player2)
    tree.insert(player3)
    tree.insert(player4)
    tree.insert(player5)
    tree.insert(player6)

    tree.search("Gabriela")
    tree.search("Maria")

    tree.traverse()

    print("\n")
    print("This is balanced tree: ")
    tree.balance_bst()


if __name__ == '__main__':
    main()