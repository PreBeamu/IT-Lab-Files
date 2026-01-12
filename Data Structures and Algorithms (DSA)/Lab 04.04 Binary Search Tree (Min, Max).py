class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        new_node = BSTNode(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def preorder(self, node=None, is_start=True):
        if not node and is_start:
            node = self.root
            print("Preorder:", end="")

        if node is None:
            return ""

        current = " -> "+str(node.data)
        left = self.preorder(node.left, False)
        right = self.preorder(node.right, False)
        
        result = current + left + right

        if is_start:
            print(result+" ")
        
        return result

    def inorder(self, node=None, is_start=True):
        if not node and is_start:
            node = self.root
            print("Inorder:", end="")

        if node is None:
            return ""

        current = " -> "+str(node.data)
        left = self.inorder(node.left, False)
        right = self.inorder(node.right, False)
        
        result = left + current + right

        if is_start:
            print(result+" ")
        
        return result

    def postorder(self, node=None, is_start=True):
        if not node and is_start:
            node = self.root
            print("Postorder:", end="")

        if node is None:
            return ""

        left = self.postorder(node.left, False)
        right = self.postorder(node.right, False)
        current = " -> "+str(node.data)
        
        result = left + right + current

        if is_start:
            print(result+" ")
        
        return result

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return
        self.preorder()
        self.inorder()
        self.postorder()

    def find_min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())

main()