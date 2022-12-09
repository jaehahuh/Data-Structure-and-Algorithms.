class MaxStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.max_stack = ArrayStack()
        
    def __len__(self):
        return self.stack.__len__()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, elem):
        self.stack.push(elem)
        if not self.max_stack or elem >= self.max():
            self.max_stack.push(elem) 

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("MaxStack is empty")
        if self.top() == self.max():
            self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("MaxStack is empty")
        return self.stack.top()

    def max(self):
        if (self.is_empty() == True):
            raise Exception("MaxStack is empty")
        return self.max_stack.top()




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



