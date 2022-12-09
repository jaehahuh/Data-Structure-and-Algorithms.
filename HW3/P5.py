def iterative_inorder(bin_tree):
    elem = bin_tree.root
    stack = []
    while True:
        if elem is not None:
            stack.append(elem)
            elem = elem.left
        elif stack:
            elem = stack.pop()
            yield elem.data
            elem = elem.right
        else:
            break











import ArrayQueue



class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            self.right = right

            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

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
        return self.subtree_sum(self.root)

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
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)

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
            yield from self.subtree_postrder(subtree_root.right)
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



'''

def main():
    left_child1 = LinkedBinaryTree.Node(7)
    right_child1 = LinkedBinaryTree.Node(4)
    left_node2 = LinkedBinaryTree.Node(9, left_child1, right_child1)
    right_child2 = LinkedBinaryTree.Node(5)
    right_node3 = LinkedBinaryTree.Node(6, None, right_child2)
    right_node2 = LinkedBinaryTree.Node(1)
    right_node1 = LinkedBinaryTree.Node(2, right_node2, right_node3)
    left_node1 = LinkedBinaryTree.Node(8, None, left_node2)
    
    bin_root = LinkedBinaryTree.Node(3, left_node1, right_node1)
    bin_tree = LinkedBinaryTree(bin_root)

    for val in iterative_inorder(bin_tree):
        print(val, end = ' ')
    print()

'''
