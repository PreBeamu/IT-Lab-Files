class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

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

        if node is None:
            return ""

        if is_start:
            print("-> "+str(node.data), end="")
        else:
            print(" -> "+str(node.data), end="")

        self.preorder(node.left, False)
        self.preorder(node.right, False)

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))

  print("Preorder: ", end="")
  my_bst.preorder()

main()