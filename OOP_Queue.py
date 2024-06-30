class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print("Queue is full. Cannot enqueue.")

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")
            
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. No front element.")

queue1 = MyQueue ( capacity =5)

queue1 . enqueue (1)

queue1 . enqueue (2)

print ( queue1 . is_full () )

print ( queue1 . front() )

print ( queue1 . dequeue () )

print ( queue1 . front() )

print ( queue1 . dequeue () )

print ( queue1 . is_empty () )
