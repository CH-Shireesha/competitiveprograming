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
            root = new_val
        else:
            if(self.root.value < self.value):
                if(self.root.right is None):
                    root.right = new_val
                else:
                    insert(self.root.right,new_val)
            else:
                if(root.left is None):
                    root.left = new_val
                else:
                    insert(root.left,new)
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