class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
            return
        result, lastN = "", self.head
        while lastN:
            result += (lastN.data+" -> ")
            lastN = lastN.next
        print(result.rstrip(" -> "))

    def insert_last(self, data):
        node = DataNode(data)
        if not self.head:
            self.head = node
            self.count += 1
            return
        lastN = self.head
        while lastN.next:
            lastN = lastN.next
        lastN.next = node
        self.count += 1

    def insert_front(self, data):
        node = DataNode(data)
        if not self.head:
            self.head = node
            self.count += 1
            return
        oldNode = self.head
        self.head = node
        node.next = oldNode
        self.count += 1

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    # elif condition == "B":
    #     mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #     mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()