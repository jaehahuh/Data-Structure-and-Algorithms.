class ArrayDeque:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None   
    
    def __len__(self):
        return self.num_of_elems
   
    def is_empty(self):
        return len(self) == 0


    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[-1]



    def enqueue_first(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        
        if self.is_empty():
            self.data[-1] = elem
            self.front_ind = -1
            self.num_of_elems += 1
        else:
            front_ind = (self.front_ind - 1) % len(self.data)
            self.data[front_ind] = elem
            self.front_ind = front_ind
            self.num_of_elems += 1    

            
        
    def enqueue_last(self, elem):
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


    def delete_first(self):
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

        
    def delete_last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        back_ind = self.data[elem]
        self.data[elem] = None
        self.back_ind = -1
        self.num_of_elems -= 1
       
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data)//2)
        return elem



    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity

        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = old_ind + 1
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0





def main():

    d1 = ArrayDeque()

    for i,k in enumerate("12345678"):
        d1.enqueue_first(k)
        print(d1.data)

    for j in range(8):
        d1.delete_first()
        print(d1.data)


    d2 = ArrayDeque()
    for i,k in enumerate("12345678"):
        d2.enqueue_last(k)
        print(d2.data)

    for j in range(8):
        d2.delete_last()
        print(d2.data)


main()


