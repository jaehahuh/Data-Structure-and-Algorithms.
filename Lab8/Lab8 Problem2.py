def right_circular_shift(lnk_lst):
    if lnk_lst.is_empty():
        raise Exception ("Linked List is empty")
    else:
        front = lnk_lst.first_node()
        last = lnk_lst.last_node()
        prev_l = last.prev
        prev_l.next = lnk_lst.trailer 
        lnk_lst.trailer.prev = prev_l
        lnk_lst.header.next = last
        last.prev = lnk_lst.header  
        last.next = front
        front.prev = last
         
        
    
        

class DoublyLinkedList:
    class Node:
        def __init__(self, data = None, prev = None, next = None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

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
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1

    def add_first(self,data):
        self.add_after(self.header, data)

    def add_last(self,data):
        self.add_after(self.trailer.prev, data)
        
    def add_before(self, node, data):

        self.add_after(self.node.prev, data)

#lnk_lst.delete_node(some_node) ==> delete_node(lnk_lst, some_node)
    def delete_node(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        data = node.data
        node.disconnect()
        self.size -= 1
        return data

    def delete_first(self):
        #self.delete_node(self.header.next)
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        #self.delete_node(self.trailer.prev)
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
        return '[' + '<---> '.join(str(item) for item in self) + ']'


lnk_lst = DoublyLinkedList()
lnk_lst.add_last(1)
lnk_lst.add_last(2)
lnk_lst.add_last(3)
lnk_lst.add_last(4)
lnk_lst.add_last(5)


print(lnk_lst)
right_circular_shift(lnk_lst)
print(lnk_lst)

