class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self) -> list:
        result = []
        def preorder(node):
            if node != None:
                result.append(node.value)  # Visit the current node
                preorder(node.left)  # Traverse the left subtree
                preorder(node.right)  # Traverse the right subtree

        preorder(self.root)
        return result

    def inorder_traversal(self) -> list:
        result = []
        def inorder(node):
            if node != None:
                inorder(node.left)
                result.append(node.value)
                inorder(node.right)
        inorder(self.root)
        return result

    def postorder_traversal(self) -> list:
        result = []
        def postorder(node):
            if node != None:
                postorder(node.left)
                postorder(node.right)
                result.append(node.value)          
        postorder(self.root)
        return result


# Create a binary tree
bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)
bt.root.left.left.left = TreeNode(8)
bt.root.left.left.right = TreeNode(9)
bt.root.right.right.right = TreeNode(10)

# Test the traversals
print("Preorder Traversal:", bt.preorder_traversal())
print("Inorder Traversal:", bt.inorder_traversal())    
print("Postorder Traversal:", bt.postorder_traversal())  

