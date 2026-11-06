"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion depends on value comparison: smaller values go to the left 
        # subtree and larger values go to the right subtree to maintain the BST property.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: if we hit a null spot, create and return the new node
        if node is None:
            return Node(value)
        
        # Recursive step: sort smaller values left, larger values right
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Note: duplicate values are ignored or can be handled depending on policy
        
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is more efficient than linear search because at each step, 
        # the tree's sorted structure allows us to discard half of the remaining 
        # search space (O(log n) time complexity on balanced trees).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        # Base case: node is null (not found) or we found the value
        if node is None:
            return False
        if node.value == value:
            return True
        
        # Search left or right depending on the comparison
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # 1. Visit left subtree (smaller values)
            self._inorder_recursive(node.left, values)
            # 2. Visit current node
            values.append(node.value)
            # 3. Visit right subtree (larger values)
            self._inorder_recursive(node.right, values)
            # In-order traversal produces sorted output because visiting 
            # the left child first ensures all smaller elements are processed 
            # before the parent, followed by all larger elements in the right child.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    bst = BST()
    # Insert at least 7 values with distribution across left/right subtrees
    # Choosing 50 as root, then spreading values out
    initial_values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values into BST: {initial_values}")
    
    for val in initial_values:
        bst.insert(val)
        
    # A BST is efficient at reducing search space because each comparison 
    # eliminates roughly half of the branches (subtrees) depending on whether 
    # the target is smaller or larger than the current node.

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_elements = bst.inorder()
    print(f"In-order Traversal Result: {sorted_elements}")
    print("Explanation: In-order traversal visits left-child, root, then right-child, "
          "which naturally outputs numbers in ascending sorted order for a BST.")

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    # Search for two existing values
    print(f"Search for 40 (Exists): {bst.search(40)}")
    print(f"Search for 70 (Exists): {bst.search(70)}")
    
    # Search for two non-existing values
    print(f"Search for 25 (Does not exist): {bst.search(25)}")
    print(f"Search for 99 (Does not exist): {bst.search(99)}")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    # Edge case: Searching or traversing an empty tree
    empty_bst = BST()
    print(f"Searching for 50 in an empty tree: {empty_bst.search(50)}")
    print(f"In-order traversal of an empty tree: {empty_bst.inorder()}")
    print("Explanation: An empty tree handles null roots gracefully by returning "
          "false during searches and an empty list during traversals without throwing errors.")


if __name__ == "__main__":
    main()