class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root == None:
            self.root = new_node
            self.size += 1
        else:
            current = self.root
            while True:
                if key >= current.value:
                    if current.right == None:
                        current.right = new_node
                        self.size += 1
                        break
                    else: current = current.right
                else:
                    if current.left == None:
                        current.left = new_node
                        self.size += 1
                        break
                    else:
                        current = current.left

    def search(self, key) -> TreeNode:
        current = self.root
        while current is not None:
            if current.value == key:
                return current
            elif key < current.value:
                current = current.left
            else:
                current = current.right
        return None
    
    def level_order_traversal(self) -> list:
        if self.root == None:
            return []
        result = []
        queue = []
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    # Define size as a regular method
    def get_size(self):
        return self.size
    


# Initialize BST.
bst = BinarySearchTree()

# Test inserting nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

# Test size method.
assert bst.get_size() == 7
assert bst.search(1) == None

# Test inserting additional nodes.
bst.insert(1)
bst.insert(6)

assert bst.get_size() == 9
assert bst.search(1).value == 1

# Finally, also test by inserting duplicate values.

# Test level order traversal with duplicates.
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(1)
bst.insert(6)

# Test level order traversal.
assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]
