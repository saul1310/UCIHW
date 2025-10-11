# # write a stack class from scratch
# required functions
# push(x)
# pop() removes top element and returns it 
# peek() show top element
# size() return the size of the stack

class stack:
    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.append(element)

    def pop(self):
        if len(self.items) == 0:
            print("unable to pop from empty stack")
        top = self.items[-1]
        self.items.pop()
        return top
    
    def peek(self):
        if len(self.items) == 0:
            print("empty stack")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

s = stack()
s.push(10)
s.push(20)
print(s.peek())   # 20
print(s.pop())    # 20
print(s.size())   # 1