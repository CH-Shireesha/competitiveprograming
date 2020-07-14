"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.insert(len(self.storage),new_element)
        print(self.storage,"iiiiii")
        pass

    def peek(self):
        return self.storage[0]
        pass  

    def dequeue(self):
        return self.storage.pop()
        pass

q = Queue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())