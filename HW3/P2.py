class Integer:
    def __init__(self, num_str):
        self.num = DoublyLinkedList()
        for i in num_str:
            self.num.add_last (int(i))

    def __add__(self,other):
        result = DoublyLinkedList()
        carry = 0
        num1 = self.num
        num2 = other.num
        last_digit1 = num1.last_node()
        last_digit2 = num2.last_node()
        while True:
            if last_digit1.data is not None and last_digit2.data is not None:
                result.add_first ((last_digit1.data + last_digit2.data+carry)%10)
                carry = (last_digit1.data+last_digit2.data + carry)//10
                last_digit1 = last_digit1.prev
                last_digit2 = last_digit2.prev
            elif last_digit1.data is not None and last_digit2.data is None:
                result.add_first ((last_digit1.data + carry)%10)
                carry = (last_digit1.data + carry)//10
                last_digit1 = last_digit1.prev
            elif last_digit1.data is None and last_digit2.data is not None:
                result.add_first ((last_digit2.data+carry)%10)
                carry = (last_digit2.data + carry)//10
                last_digit2 = last_digit2.prev         
            elif last_digit1.data is None and last_digit2.data is None and carry != 0:
                result.add_first ((carry)%10)
                carry = (carry)//10
            elif last_digit1.data is None and last_digit2.data is None and carry == 0:
                break   
        return result


    def __repr__(self):
        num = self.num.first_node()
        s=" "
        while num.data is not None:
            s+= str(num.data)
            num = num.next
        return s











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
        return '[' + '<---> '.join(str(item) for item in self) + ']'




'''
def main():
    num1 = Integer('127')
    num2 = Integer('974')
    num3 = num1 + num2
    print("num3: ", Integer(num3) )

'''
