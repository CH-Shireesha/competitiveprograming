"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here

        pass
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        n = 1
        temp = self.head
        if (temp == None):
            return None
        while (n < position and temp.next != None):
            print(position, n, "----", temp.value)
            temp = temp.next
            n = n+1
        if n != position:
            return None
        return temp
        pass
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        n = 1
        temp = self.head
        if (position == 1):
            self.head = new_element
            self.head.next = temp
        else:
            while (n < position):
                temp = temp.next
                n = n + 1
            current = temp.next
            temp.next = new_element
            new_element.next = current
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp = self.head
        if (temp.value == value):
            self.head = temp.next
            return
        while (temp.next == None):
            if(temp.next.value == value):
                temp.next = temp.next.next
                return
            temp = temp.next
