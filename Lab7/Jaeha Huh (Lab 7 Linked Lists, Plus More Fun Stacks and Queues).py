#Problem1. Linked Stack
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



#Problem2-1. LeakyStack(Array)
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


#Problem2-2. LeakyStack(Linked)
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
            



#3. Stacks with Queues
class Qstack:
    
    def __init__(self):
        self.data_queue = ArrayQueue()

    def __len__(self):
        return len(self.data_queue)

    def is_empty(self):
        return len(self.data_queue) == 0

    #O(1)
    def push (self, elem):
        self.data_queue.enqueue(elem)

    #O(n)
    def pop(self):
        if self.is_empty():
            raise Exception("Qstack is empty")
        for i in range (len(self.data_queue) - 1 ):
            elem = self.data_queue.dequeue()
            self.data_queue.enqueue(elem)
        return self.data_queue.dequeue()
        
    def top(self):
        if self.is_empty():
            raise Exception("Qstack is empty")
        for i in range (len(self.data_queue) ):
            elem = self.data_queue.dequeue()
            self.data_queue.enqueue(elem)
            
        return elem






#DoublyLinkedList
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


#Array Queue
class ArrayQueue:
    INITIAL_CAPACITY = 8
       
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None
        
    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1
            
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data)//2)
        return elem
        

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]


    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity

        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = old_ind + 1
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0




#Test codes
def main():
    #Problem1. Test codes
    print("Test codes : LinkedStack")
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

    #Problem2-1. Test codes
    print()
    print("Test codes : ArrayLeakyStack")
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

    #Problem2-2. Test codes
    print()
    print("Test codes : LinkedLeakyStack")
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


    #Problem3. Test codes
    print()
    print("Test codes : QStack")
    s3 = Qstack()
    s3.push(1)
    s3.push(2)
    s3.push(3)
    s3.push(4)
    s3.push(5)
    s3.push(6)
    s3.push(7)
    s3.push(8)


    print(s3.data_queue.data)
    print('top:', s3.top())
    print(s3.data_queue.data)
    print('pop:', s3.pop())
    print('pop:', s3.pop())
    print('pop:', s3.pop())
    print(s3.data_queue.data)
    print('top:', s3.top())


main()
