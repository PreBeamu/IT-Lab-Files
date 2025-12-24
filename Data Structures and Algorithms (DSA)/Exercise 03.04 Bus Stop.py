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

    def get_nodes(self):
        if not self.head:
            return ""
        result, lastN = "", self.head
        while lastN:
            result += (lastN.data+",")
            lastN = lastN.next
        return result.rstrip(",")

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
        self.count += 1

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

    def getIndex(self, index, returnNode=False):
        currIndex, lastN = 1, self.head
        if self.count < index or index <= 0:
            return "Error"
        while lastN:
            if currIndex >= index:
                return lastN.data if not returnNode else lastN
            lastN = lastN.next
            currIndex += 1

    def insert_Index(self, index, data):
        self.count += 1
        if index == 1:
            newNode = DataNode(data)
            afterNode = self.head
            self.head = newNode
            newNode.next = afterNode
        elif index < self.count:
            newNode = DataNode(data)
            beforeNode = self.getIndex(index-1,True)
            afterNode = self.getIndex(index,True)
            beforeNode.next = newNode
            newNode.next = afterNode
        else:
            self.insert_last(data)

def main():
    bus = SinglyLinkedList()
    max_passen, sign = int(input()), int(input())
    done = 0
    for num in range(1,sign+1):
        # print("----------- REACHED SIGN",num,"-----------")
        line = input().strip()
        i = 0

        while i < len(line) and line[i] != ' ':
            i += 1
        while i < len(line) and line[i] == ' ':
            i += 1

        data = line[i:]
        if not data: continue
    
        current_passen = bus.get_nodes().split(",")
        for des in current_passen:
            if des and int(des) == num:
                bus.delete(des)
                done += 1
                # print("EJECTED",des)

        for des in data.split(" "):
            if not des.isdigit(): continue
            if bus.count < max_passen and int(des) > num:
                bus.insert_last(des)
                # print("PICKED UP",des)

    print(done)

main()
