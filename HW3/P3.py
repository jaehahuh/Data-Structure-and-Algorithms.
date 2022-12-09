def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(lst1_node, lst2_node, merged_lst):
                if lst1_node.data is None and lst2_node.data is None:
                        return merged_lst
                elif lst2_node.data is None and lst1_node.data is not None:
                    merged_lst.add_last(lst1_node.data)
                    merge_sublists(lst1_node.next, lst2_node, merged_lst)
                    return merged_lst
                elif lst1_node.data is None and lst2_node.data is not None:
                    merged_lst.add_last(lst2_node.data)
                    merge_sublists(lst1_node, lst2_node.next, merged_lst)
                    return merged_lst
                else:
                    if lst1_node.data < lst2_node.data:
                        merged_lst.add_last(lst1_node.data)
                        merge_sublists(lst1_node.next, lst2_node, merged_lst)
                        return merged_lst
                    else: #lst1_node.data >= lst2_node.data:
                        merged_lst.add_last(lst2_node.data)
                        merge_sublists(lst1_node, lst2_node.next, merged_lst)
                        return merged_lst
    merged_lst = DoublyLinkedList()
    return  merge_sublists(srt_lnk_lst1.first_node(), srt_lnk_lst2.first_node(), merged_lst)










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

    lnk_lst1 = DoublyLinkedList()
    lnk_lst1.add_last(1)
    lnk_lst1.add_last(3)
    lnk_lst1.add_last(6)

    lnk_lst2 = DoublyLinkedList()
    lnk_lst2.add_last(2)
    lnk_lst2.add_last(3)
    lnk_lst2.add_last(5)
    lnk_lst2.add_last(10)

    merged_lst = merge_linked_lists(lnk_lst1, lnk_lst2)
    print(merged_lst)

'''
