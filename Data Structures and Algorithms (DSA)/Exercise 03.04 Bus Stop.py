class DataNode:
    def __init__(self, v):
        self.v = v
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_last(self, data):
        """Insert new node as last one."""
        node = DataNode(data)
        self.count += 1
        if not self.head:
            self.head = node
            return
        lastN = self.head
        while lastN.next:
            lastN = lastN.next
        lastN.next = node

    def remove_front(self):
        if self.head is None:
            return None
        v = self.head.v
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return v


def read_next(txt):
    num, seen = 0, False
    for i in txt:
        if '0' <= i <= '9':
            num = num * 10 + int(i)
            seen = True
        elif seen:
            return num
    return num if seen else None


def main():
    maxPassengers = int(input())
    busStops = int(input())
    routes = SinglyLinkedList()

    while busStops > 0:
        routes.insert_last(input())
        busStops -= 1

    bus = SinglyLinkedList()
    done, stop = 0, 1

    while stop <= busStops:
        rem_routes = SinglyLinkedList()
        active_it = None

        while routes.count > 0:
            line = routes.remove_front()
            it = iter(line)
            start = read_next(it)
            if start == stop and active_it is None:
                active_it = it
            else:
                rem_routes.insert_last(line)

        routes = rem_routes
        rem_bus = SinglyLinkedList()
        while bus.count > 0:
            d = bus.remove_front()
            if d == stop:
                done += 1
            else:
                rem_bus.insert_last(d)
        bus = rem_bus

        if active_it is not None:
            while True:
                d = read_next(active_it)
                if d is None:
                    break
                if d > stop and bus.count < maxPassengers:
                    bus.insert_last(d)
        stop += 1
    print(done)

main()
