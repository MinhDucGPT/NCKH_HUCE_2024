class MyStack():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        if (self.stack is None):
            return True
        else:
            return False
    
    def is_full(self):
        if(len(self.stack)== self.capacity):
            return True 
        else:
            return False
    
    def pop(self):
        return self.stack.pop(-1)
        
        
    def push(self, value):
        self.stack.append(value)
    
    def top(self):
        return self.stack[-1]
    
stack1 = MyStack ( capacity =5)

stack1 . push (1)

stack1 . push (2)  

print ( stack1 . is_full () )
    
print ( stack1 . top () )    

print ( stack1 . pop () )

print ( stack1 . top () )

print ( stack1 . pop () )

print ( stack1 . is_empty () )