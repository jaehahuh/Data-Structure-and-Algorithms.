class EmptyCollection(Exception):
    pass

class DupStack:
    def __init__(self):
        self.data_stack = Stack()
        self.size = 0

    def __len__(self):
        return self.size
        
    def is_empty(self):
        return len(self) == 0

    def push(self,e):
        if self.data_stack.is_empty():
            self.data_stack.push ((e, 1))
        else:
            top_elem, dup_count = self.data_stack.top()
            if  top_elem == e:
                self.data_stack.pop()
                self.data_stack.push ((top_elem, dup_count+1)) #tuple
            else:
                self.data_stack.push((e, 1))
        self.size += 1

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        #top_elem, dup_count = self.data_stack.top()
        #return top_elem
        return self.data_stack.top()[0]
    
    def top_dups_count(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        #top_elem, dup_count = self.data_stack.top()
        #return dup_count
        return self.data_stack.top()[1]

    def pop(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        top_elem, dup_count = self.data_stack.pop()
        dup_count -= 1
        if dup_count > 0:
            self.data_stack.push((top_elem, dup_count))
        self.size -= 1
        return top_elem 


    def pop_dups(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        top_elem, dup_count = self.data_stack.pop()
        self.size -= dup_count
        return top_elem
