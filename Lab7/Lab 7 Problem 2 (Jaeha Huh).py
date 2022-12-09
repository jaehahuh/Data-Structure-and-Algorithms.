class ArrayLeakyStack:
    def __init__(self, max_num_of_elems):
        self.data = [None] * max_num_of_elems
        self.max = max_num_of_elems
        self.front = 0
        self.r = 0
        
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data[self.front] = item
        self.front = (self.front + 1) % len(self.data)
      
        
    def pop(self):
        if self.is_empty():
            raise Exception("ArrayLeakyStack is empty")
        pop = self.data[self.front - 1]
        self.data[self.front - 1] = None
        self.front = (self.front - 1) % self.max
        return pop
            
        
    def top(self):
        if self.is_empty():
            raise Exception ("ArrayLeakyStack is empty")
        top = self.data[self.front - 1]
        return top



        
class LinkedLeakyStack:
    def __init__(self, max_num_of_elems):
        self.data = DoublyLinkedList()
        self.max = max_num_of_elems
        
    def __len__(self):
        return len(self.data)
        
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, elem):
        if (len(self.data) < self.max):
            self.data.add_last(elem)
        else:
            self.data.add_last(elem)
            self.data.delete_first()

    def pop(self):
        if self.is_empty():
            raise Exception("LinkedLeakyStack is empty")
        elem = self.data.last_node().data
        self.data.delete_last()
        return elem

    def top (self):
        if self.is_empty():
            raise Exception("LinkedLeakyStack is empty")
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
    s1 = ArrayLeakyStack(5)
    s1.push (17)
    s1.push (42)
    s1.push (6)
    s1.push (31)
    s1.push (28)
    s1.push (2)

    print(s1.data)
    print(s1.top())
    print(s1.pop())
    print(s1.data)


    s2 = LinkedLeakyStack(5)
    s2.push(17)
    s2.push(42)
    s2.push(6)
    s2.push(31)
    s2.push(28)
    s2.push(2)
    
    print(s2.data)
    print(s2.top())
    print(s2.pop())
    print(s2.data)




main()
