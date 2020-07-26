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
        if(self == None):
            self = new_val
        else:
            if(self.value < node.value):
                if(self.right is None):
                    self.right = new_val
                else:
                    insert(self.right,new_val)
            else:
                if(self.left is None):
                    self.left = new_val
                else:
                    insert(self.left,new_val)
        pass

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass

