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
        temp = self.root
        while(True):
            if(temp.value > new_val and temp.left is None):
                temp.left = Node(new_val)
                return
            elif(temp.value < new_val and temp.right is None):
                temp.right = Node(new_val)
                return
            if(temp.value > new_val):
                temp = temp.left
            elif(temp.value < new_val):
                temp = temp.right

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        temp = self.root
        while(temp):
            if(temp.value == find_val):
                return True
            elif(temp.value > find_val):
                temp = temp.left
            elif(temp.value <= find_val):
                temp = temp.right
        return False

tree = BST(4)
tree.insert(6)
tree.insert(7)
print(tree.search(4))