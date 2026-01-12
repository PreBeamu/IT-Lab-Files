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
    
    def get_height(self, node=None, is_start=True):
        if is_start:
            if self.is_empty():
                return 0
            node = self.root

        if node is None:
            return 0

        left_height = self.get_height(node.left, False)
        right_height = self.get_height(node.right, False)

        return 1 + max(left_height, right_height)

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
    
    def delete(self, req):
        if self.is_empty():
            print("Delete Error, "+str(req)+" is not found in Binary Search Tree.")
            return False

        parent = None
        current = self.root

        while current and current.data != req:
            parent = current
            if req < current.data:
                current = current.left
            else:
                current = current.right
        if current is None:
            print("Delete Error, "+str(req)+" is not found in Binary Search Tree.")
            return False
        
        # Both Subtrees
        if current.left and current.right:
            succ_root = current
            succ = current.left
            while succ.right:
                succ_root = succ
                succ = succ.right
            current.data = succ.data
            parent = succ_root
            current = succ

        child = current.left if current.left else current.right

        if parent is None:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child
        return True

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      print(my_bst.get_height())
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")

main()