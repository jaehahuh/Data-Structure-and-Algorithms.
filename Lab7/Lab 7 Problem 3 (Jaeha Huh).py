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
    s = Qstack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)


    print(s.data_queue.data)
    print('top:', s.top())
    print(s.data_queue.data)
    print('pop:', s.pop())
    print('pop:', s.pop())
    print('pop:', s.pop())
    print(s.data_queue.data)
    print('top:', s.top())

main()

