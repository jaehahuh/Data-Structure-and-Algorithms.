class Queue:
    def __init__(self):
        self.in_data = ArrayStack()
        self.out_data = ArrayStack()

    def __len__(self):
        return (self.in_data.__len__() + self.out_data.__len__())
        
    def is_empty(self):
        return self.in_data.is_empty() and self.out_data.is_empty()

    def enqueue(self, elem):
        self.in_data.push(elem)

    def dequeue(self):
        if self.out_data.is_empty() and self.in_data.is_empty():
            raise Exception("Queue is empty")
        if self.out_data.is_empty():
            while not self.in_data.is_empty():
                elem = self.in_data.pop()
                self.out_data.push(elem)
        return self.out_data.pop()

    def front(self):
        if self.out_data.is_empty() and self.in_data.is_empty():
            raise Exception("Queue is empty")
        if self.out_data.is_empty():
            while not self.in_data.is_empty():
                elem = self.in_data.pop()
                self.out_data.push(elem)        
        return self.out_data.top()
        


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]



