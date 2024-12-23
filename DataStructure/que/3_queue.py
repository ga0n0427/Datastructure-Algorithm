class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, data):
        if self.length == 0:
            self.front = self.rear = Node(data)
        else:
            node = Node(data)
            self.rear.next = node
            self.rear = node
        self.length += 1
            
    def dequeue(self):
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.length -= 1
        return data
    
    def is_Empty(self):
        return self.front is None
    
if __name__== "__main__" :
    q = Queue()
    
    empty = q.is_empty()
    print(empty)
    q.enqueue(1)
    q.enqueue(2)    
    q.enqueue(2)
    
    print(q)
    
    first = q.dequeue()
    print(first)
    
    second = q.dequeue()
    print(second)
    
    third = q.dequeue()
    print(third)