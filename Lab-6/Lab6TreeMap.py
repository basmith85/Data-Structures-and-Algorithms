class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, root, key, value):
        if root == None:
            return TreeNode(key, value)
        
        if key < root.key:
            root.left = self._put(root.left, key, value)
        elif key > root.key:
            root.right = self._put(root.right, key, value)
        else:
            root.value = value
        return root
    
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, root, key):
        if root == None:
            return None
        if key < root.key:
            return self._get(root.left, key)
        elif key > root.key:
            return self._get(root.right, key)
        else:
            return root.value
        
# TreeMap.

# Create a TreeMap
tree_map = TreeMap()

# Test putting and getting key-value pairs.
tree_map.put(3, "A")
tree_map.put(1, "B")
tree_map.put(2, "C")
tree_map.put(4, "D")

assert tree_map.get(2) == "C"
assert tree_map.get(1) == "B"
assert tree_map.get(4) == "D"
# Non-existent key should return None.
assert tree_map.get(5) is None
