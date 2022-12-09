import ArrayQueue


def count_val (root, value):
    tree = LinkedBinaryTree(root)
    count = 0
    for i in tree.preorder():
        if i == value:
            count+=1
    return count





class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left = None, right = None): #initialize Node
            self.data = data
            self.parent = None
            self.left = left     #left child
            self.right = right    #right child

            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root = None):   #initialize LinkedBinaryTree
        self.root = root
        self.size = self.subtree_count(root)


    # Returns number of nodes in the subtree rooted by "subtree_root"
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
            #right is not None (but left is)
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            #left is not None (but right is)
            return 1 + self.subtree_height(subtree_root.left)
        else:
            #left and right are both are not None
            left_height = self.subtree_height(subtree.left)
            right_height = self.subtree_height(subtree.right)

            return 1 + max(left_height, right_height) 
    
    def preorder(self):
        yield from self.subtree_preorder(self.root)   #yield from : yield as generator, keep calling next

    # yields all values in the nodes of the subtree rooted at "subtree_root" in preorder
    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            #order doesn't matter (they yield all values)
            yield subtree_root.data        
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)   

    # yields all values in the nodes of the subtree rooted at "subtree_root" in postorder
    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root.data



    def inorder(self):
        yield from self.subtree_inorder(self.root)   

    # yields all values in the nodes of the subtree rooted at "subtree_root" in postorder
    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


  
    #"Level Order" Traversal == Breadth_first
    #use ArrayQueue
    def breadth_first(self):
        if self.is_empty():
            return
        node_queue = ArrayQueue.ArrayQueue()   #filename. classname()
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



left_child1 = LinkedBinaryTree.Node(6)
right_child1 = LinkedBinaryTree.Node(8)
root_node1 = LinkedBinaryTree.Node(5, left_child1, right_child1)
my_tree1 = LinkedBinaryTree(root_node1)

left_child2 = LinkedBinaryTree.Node(9)
right_child2 = LinkedBinaryTree.Node(10)
root_node2 = LinkedBinaryTree.Node(8, left_child2, right_child2)
my_tree2 = LinkedBinaryTree(root_node2)

super_root = LinkedBinaryTree.Node(4, root_node1, root_node2)
super_tree = LinkedBinaryTree(super_root)

for val in super_tree.preorder():
    print(val, end= " ")

print()
print()


print(count_val(super_root, 10))


