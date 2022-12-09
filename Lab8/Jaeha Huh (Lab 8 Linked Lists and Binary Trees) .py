#1 Written Problems

#1. Give the preorder, inorder, and postorder traversals of the tree.
#Ans: preorder =  ABDGCEFH,   inorder = GDBAECFH,   postorder = GDBEHFCA

#2. What is the total height of the tree? 
#Ans: 3
#3. What is the depth of node D?.
#Ans: 2




#2 Circular Shift Linked List
def right_circular_shift(lnk_lst):
    if lnk_lst.is_empty():
        raise Exception ("Linked List is empty")
    else:
        front = lnk_lst.first_node()
        last = lnk_lst.last_node()
        prev_l = last.prev
        prev_l.next = lnk_lst.trailer 
        lnk_lst.trailer.prev = prev_l  
        last.next = front
        front.prev = last
        last.prev = lnk_lst.header   
        lnk_lst.header.next = last

#3 Count Values in Binary Tree 
def count_val (root, value):
    tree = LinkedBinaryTree(root)
    count = 0
    for i in tree.preorder():
        if i == value:
            count+=1
    return count


#4 Invert a Binary Tree 
def invert_binary_tree(bin_tree):
    root = bin_tree.root
    def invert_binary_tree_helper(root):
        if root is None:
            return None
        root.left, root.right = invert_binary_tree_helper(root.right), invert_binary_tree_helper(root.left)
        return root
    return invert_binary_tree_helper(root)



#5 Count Number of leaves, 1-child, and 2-child nodes 
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.parent = None
            self.left = left     
            self.right = right   

            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root = None):   
        self.root = root
        self.size = self.subtree_count(root)

############## Problem 5 codes #############
    def subtree_children_dist(self, subtree_root):
        lst = []
        lst.append(self.count_leaves(subtree_root))
        lst.append(self.count_one_child(subtree_root))
        lst.append(self.count_two_children(subtree_root))
        return lst
        

    def count_leaves(self, subtree_root):
        if subtree_root is None:
            return 0
        if subtree_root.left is None and subtree_root.right is None:
            return 1
        else:
            return self.count_leaves(subtree_root.left) + self.count_leaves(subtree_root.right)

    def count_one_child(self, subtree_root):
        if subtree_root is None:
            return 0
        if subtree_root.left is None and subtree_root.right is not None:
            return 1
        if subtree_root.left is not None and subtree_root.right is None:
            return 1
        else:
            return self.count_one_child(subtree_root.left) + self.count_one_child(subtree_root.right)

    def count_two_children(self, subtree_root):
        if subtree_root is None:
            
            return 0
        if subtree_root.left is not None and subtree_root.right is not None:
            return 1 + self.count_two_children(subtree_root.left) + self.count_two_children(subtree_root.right)
        else:
            return self.count_two_children(subtree_root.left) + self.count_two_children(subtree_root.right)
################################################
        
    def subtree_count(self, subtree_root):
        if subtree_root is None:
            return 0
        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)

        return left_count + right_count + 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum (self.root)

    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)

        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:   
            return 0
        elif subtree_root.left is None:
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:  
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree.left)
            right_height = self.subtree_height(subtree.right)

            return 1 + max(left_height, right_height) 
    
    def preorder(self):
        yield from self.subtree_preorder(self.root)   

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
           
            yield subtree_root.data        
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)   


    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root.data



    def inorder(self):
        yield from self.subtree_inorder(self.root)   

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


  
    def breadth_first(self):
        if self.is_empty():
            return
        node_queue = ArrayQueue.ArrayQueue()  
        node_queue.enqueue(self.root)
        while node_queue.is_empty() == False:
            curr_node = node_queue.dequeue()
            yield curr_node
            if curr_node.left is not None:
                node_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                node_queue.enqueue(curr_node.right)
          
        
    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
        




#DoublyLinkedList
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


#ArrayQueue
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
#Test codes #2
    print("Problem 2 Circular Shift Linked List: Test code ") 

    lnk_lst = DoublyLinkedList()
    lnk_lst.add_last(1)
    lnk_lst.add_last(2)
    lnk_lst.add_last(3)
    lnk_lst.add_last(4)
    lnk_lst.add_last(5)

    print(lnk_lst)
    right_circular_shift(lnk_lst)
    print(lnk_lst)
    print()
    #Test codes #3
    print("Problem 3 Count Values in Binary Tree: Test code ")
    
    left_child1 = LinkedBinaryTree.Node(6)
    right_child1 = LinkedBinaryTree.Node(8)
    root_node1 = LinkedBinaryTree.Node(5, left_child1, right_child1)
    
    left_child2 = LinkedBinaryTree.Node(9)
    right_child2 = LinkedBinaryTree.Node(10)
    root_node2 = LinkedBinaryTree.Node(8, left_child2, right_child2)

    super_root = LinkedBinaryTree.Node(3, root_node1, root_node2)
    super_tree = LinkedBinaryTree(super_root)

    for val in super_tree.preorder():
        print(val, end= " ")
    print()
    print(count_val(super_root, 8))

    print()
    #Test codes #4
    print("Problem 4 Invert a Binary Tree : Test code ")
    left_child1 = LinkedBinaryTree.Node(4)
    right_child1 = LinkedBinaryTree.Node(5)
    root_node1 = LinkedBinaryTree.Node(2, left_child1, right_child1)


    left_child2 = LinkedBinaryTree.Node(6)
    right_child2 = LinkedBinaryTree.Node(7)
    root_node2 = LinkedBinaryTree.Node(3, left_child2, right_child2)
 

    super_root = LinkedBinaryTree.Node(1, root_node1, root_node2)
    super_tree = LinkedBinaryTree(super_root)

    for val in super_tree.preorder():
        print(val, end= " ")

    print()


    invert_binary_tree(super_tree)
    for val in super_tree.preorder():
        print(val, end= " ")

    print()
    print()
    #Test codes #5
    print("Problem 5 Count Number of leaves, 1-child, and 2-child nodes: Test code ") 
    left_child1 = LinkedBinaryTree.Node(4)
    right_child1 = LinkedBinaryTree.Node(5)
    root_node1 = LinkedBinaryTree.Node(2, left_child1, right_child1)
  
    left_child2 = LinkedBinaryTree.Node(6)
    right_child2 = LinkedBinaryTree.Node(7)
    root_node2 = LinkedBinaryTree.Node(3, left_child2, right_child2)

    super_root = LinkedBinaryTree.Node(1, root_node1, root_node2)
    super_tree = LinkedBinaryTree(super_root)


    for val in super_tree.preorder():
        print(val, end= " ")

    print()
    print()


    print("leaves: ", super_tree.count_leaves(super_root))
    print("node with one child: ", super_tree.count_one_child(super_root))
    print("node with two children: ",super_tree.count_two_children(super_root))
    print(super_tree.subtree_children_dist(super_root))

main()
