from player import Player
from player_bnode import PlayerBNode

class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    def insert(self, player: Player):
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
        return self.prepare_search(self._root, name)

    def prepare_search(self, current, name):
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
        nodes = []
        print("In-order traversal: ")
        self.in_order_helper(self._root, nodes)
        return nodes

    def in_order_helper(self, node, nodes):
        if node is not None:
            self.in_order_helper(node.left, nodes)
            nodes.append(node)
            print(str(node.player))
            self.in_order_helper(node.right, nodes)

    def balanced_tree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        self._root = PlayerBNode(nodes[mid])
        self._root.left = self.balanced_tree(nodes, start, mid -1)
        self._root.right = self.balanced_tree(nodes, mid + 1, end)
        return self._root

    def balance_bst(self):
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