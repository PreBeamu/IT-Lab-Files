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
        self.count += 1
        if not self.head:
            self.head = node
            return
        lastN = self.head
        while lastN.next:
            lastN = lastN.next
        lastN.next = node

    def insert_front(self, data):
        node = DataNode(data)
        self.count += 1
        if not self.head:
            self.head = node
            return
        oldNode = self.head
        self.head = node
        node.next = oldNode

    def insert_before(self, node, data):
        founded, lastN = "", self.head
        ##
        while lastN:
            if lastN.data == node:
                founded = True
            lastN = lastN.next
        if not founded:
            print("Cannot insert,",node,"does not exist.")
            return
        ##
        self.count += 1
        if self.head.data == node:
            self.insert_front(data)
            return
        beforeNode = DataNode(data)
        lastN, afterNode = self.head, None
        while lastN.next:
            if lastN.next.data == node:
                afterNode = lastN.next
                break
            lastN = lastN.next
        lastN.next = beforeNode
        beforeNode.next = afterNode

    def delete(self, data):
        founded, lastN = "", self.head
        ##
        while lastN:
            if lastN.data == data:
                founded = True
            lastN = lastN.next
        if not founded:
            print("Cannot delete,",data,"does not exist.")
            return
        ##
        beforeNode, afterNode, lastN = None, None, self.head
        self.count -= 1
        if self.head.data == data:
            self.head = self.head.next
            return
        while lastN.next:
            if lastN.next.data == data:
                beforeNode = lastN
                afterNode = lastN.next.next
                break
            lastN = lastN.next
        beforeNode.next = afterNode

    def getIndex(self, index):
        currIndex, lastN = 1, self.head
        if self.count < index or index <= 0:
            return "Error"
        while lastN:
            if currIndex >= index:
                return lastN.data
            lastN = lastN.next
            currIndex += 1

def main():
    mylist = SinglyLinkedList()
    text = input()
    while True:
        text = input()
        if text == "Last":
            break
        mylist.insert_last(text)
    print(mylist.getIndex(int(input())))

main()