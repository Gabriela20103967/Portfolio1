# Portfolio 4 - Knowledge Question  

1. In your own words, describe what a Binary Search Tree (BST)?. In addition, describe two important properties of a BST:
   depth and height. How are they different?

- A Binary Search Tree is a data structure that we used to organize and store data in a sorted manner, where each node has
at most two children, with the left child containing values less than the parent node and the right child containing values
greater than the parent node.

- Depth = The depth of a node in a BST is the number of edges from the node to the tree's root.
- Height = The height of a node is the number of edges from the node to the farthest leaf (the deepest node) in its subtree.

2. In your own words, describe how an algorithm to find an item in a Binary Search Tree works?
- To find an item in a Binary Search Tree, start at the root, compare the target value with the root's values. If they 
match, the search is complete. If the target is smaller, move to the left child; if larger, move to the right child. 
Repeat this process at each node until the target is found or a leaf node is reached, indicating the item is not in the
tree.

3. In your own words, describe what a Balanced BST is?
- A Balance Binary Tree is one in which the height difference between the left and right subtree of each node is less
than one. So with this height measures ensures that the operations like insertion, deletion and searching remain efficient. 

8. With the newly balanced BST, how many steps does it take at most to find an existing item in the search tree?  
- In a balanced Binary Searched Tree, the maximum number of steps to find an existing item is proportional to the tree's
height. The height of balanced BST with n nodes is approximately log2(n). 

# References 


