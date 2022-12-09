class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        
    def __len__(self):
        return len(self.data)

    def is_empty (self):
        return (len(self.data) == 0)

    def push (self, elem):
        self.data.add_last(elem)

    def pop (self):
        if self.is_empty():
            raise Exception("Linked Stack is empty")
        elem = self.data.last_node().data
        self.data.delete_last()
        return elem

    def top (self):
        if self.is_empty():
            raise Exception("Linked Stack is empty")
        return self.data.last_node().data





class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None
            
    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def add_first(self, data):
        self.add_after(self.header, data)

    def add_last(self, data):
        self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        self.add_after(self.node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        node.disconnect()
        self.size -= 1
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.first_node()
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next

    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) + ']'




#Test codes
def main():
    s = LinkedStack()
    s.push (1)
    s.push (2)
    s.push (3)
    s.push (4)
    s.push (5)

    print(s.data)
    print("top:", s.top())
    print("pop:", s.pop())
    print("pop:", s.pop())
    print(s.data)

main()


