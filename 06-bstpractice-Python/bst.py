class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        if(self.root == None):
            self.root = Node(new_val)
        else:
            if(self.root.value < new_val):
                if(self.root.right is None):
                    self.root.right = Node(new_val)
                else:
                    self.insert(self.root.right.value)
            else:
                if(self.root.left is None):
                    self.root.left = Node(new_val)
                else:
                    self.insert(self.root.left.value)
        pass

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass

tree = BST(4)
print(tree.insert(6))
print(tree.insert(7))