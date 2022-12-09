def are_bst_keys_same(bst1, bst2):
    bst1_lst = []
    bst2_lst = []
    
    for node in bst1.inorder():
        bst1_lst.append(node.item.key)
    for node in bst2.inorder():
        bst2_lst.append(node.item.key)

    return (bst1_lst == bst2_lst)




class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    # END OF Item class

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
    # END OF Node class

    # Constructor for BinarySearchTreeMap
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    # Allows for syntax: m[k] (returns the value associated with key k)
    # Raises Exception if the key is not found
    def __getitem__(self, key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) + " is not in the map")
        else:
            return node.item.value

    # Returns None if the key is not found
    def find(self, key):
        curr_node = self.root
        while curr_node is not None:
            if key == curr_node.item.key:
                return curr_node
            elif key < curr_node.item.key:
                curr_node = curr_node.left
            else: # key > curr_node.item.key
                curr_node = curr_node.right
        return None

    # Allows for syntax: m[key] = val (associates key `key` with value `val`)
    def __setitem__(self, key, value):
        node = self.find(key)
        if node is None:
            self.insert(key, value)
        else:
            node.item.value = value

    # Assumes key is not in the map
    # Insert (key, value) into subtree rooted by curr_node
    def insert(self, key, value):
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)

        if self.is_empty():
            self.root = new_node
            self.size = 1
        else:
            next_node = self.root
            while next_node is not None:
                curr_node = next_node
                if key < curr_node.item.key:
                    next_node = curr_node.left
                else: # key > curr_node.item.key
                    next_node = curr_node.right
            # insert the node
            if key < curr_node.item.key:
                curr_node.left = new_node
            else: # key > curr_node.item.key
                curr_node.right = new_node
            new_node.parent = curr_node
            self.size += 1

    # Allows for the syntax 'del map[key]'
    def __delitem__(self, key):
        node = self.find(key)
        if node is None:
            raise Exception(str(key) + " is not in the map")
        else:
            self.delete_node(node)

    # Assumes key to delete is in the tree
    def delete_node(self, node_to_delete):
        item_to_delete = node_to_delete.item
        num_children = node_to_delete.num_children()

        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 1:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                    self.root.parent = None
                    node_to_delete.disconnect()
                self.size -= 1
            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)
        else: #node_to_delete is not the root
            if num_children == 0:
                # node_to_delete is a leaf node
                parent = node_to_delete.parent
                if node_to_delete is parent.left:
                    # node_to_delete is the left child
                    parent.left = None
                else:
                    # node_to_delete is the right child
                    parent.right = None
                node_to_delete.disconnect()
            elif num_children == 1:
                parent = node_to_delete.parent
                child = None
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                if node_to_delete is parent.left:
                    # node_to_delete is left child
                    parent.left = child
                else:
                    # node_to_delete is right child
                    parent.right = child

                child.parent = parent
                node_to_delete.disconnect()
                self.size -= 1
            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                # delete max_of_left
                self.delete_node(max_of_left)

    def subtree_max(subtree_root):
        #if subtree_root.right is None:
            #return subtree_root
        #else:
            #return subtree_max(subtree_root.right)
        curr_node = subtree_root
        while curr_node.right is not None:
            curr_node = curr_node.right
        return curr_node

    def inorder(self):
        #for node in self.subtree_inorder(self, self.root):
        #    yield node
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key



def main():
    bst1 = BinarySearchTreeMap()
    bst1[20] = 1
    bst1[10] = 2
    bst1[8] = 3
    bst1[15] = 4
    bst1[28] = 5
    bst1[22] = 6
    bst1[25] = 7
    bst1[50] = 8

    for val in bst1.__iter__():
        print(val)

    #for node in bst1.inorder():
        #print(node.item.key)

    bst2 = BinarySearchTreeMap()
    bst2[20] = 1
    bst2[8] = 2
    bst2[15] = 3
    bst2[10] = 4
    bst2[22] = 5
    bst2[25] = 6
    bst2[50] = 7
    bst2[28] = 8

    for val in bst2.__iter__():
        print(val)


    print(are_bst_keys_same(bst1,bst2))


main()
