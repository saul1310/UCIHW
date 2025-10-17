# # write a stack class from scratch
# required functions
# push(x)
# pop() removes top element and returns it 
# peek() show top element
# size() return the size of the stack

class Stack:
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
    




def calculate(expression: str):
    """Converts infix (no parentheses) to postfix and evaluates it."""

    def infix_to_postfix(expr: str) -> str:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        stck = stack()
        output = []

        # Remove whitespace
        expr = expr.replace(" ", "")

        # Tokenize expression into numbers and operators
        tokens = []
        num = ""
        for ch in expr:
            if ch.isdigit():
                num += ch
            else:
                if num:
                    tokens.append(num)
                    num = ""
                tokens.append(ch)
        if num:
            tokens.append(num)

        # Infix → Postfix conversion
        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token in precedence:
                while (stck.size() > 0 and
                       precedence.get(stck.peek(), 0) >= precedence[token]):
                    output.append(stck.pop())
                stck.push(token)

        while stck.size() > 0:
            output.append(stck.pop())

        return ' '.join(output)

    # Convert and print postfix
    postfix = infix_to_postfix(expression)
    print("Postfix:", postfix)

    # Evaluate the postfix expression
    eval_stack = stack()
    for token in postfix.split():
        if token.isdigit():
            eval_stack.push(float(token))
        else:
            b = eval_stack.pop()
            a = eval_stack.pop()
            if token == '+':
                eval_stack.push(a + b)
            elif token == '-':
                eval_stack.push(a - b)
            elif token == '*':
                eval_stack.push(a * b)
            elif token == '/':
                eval_stack.push(a / b)

    result = eval_stack.pop()
    print("Result:", result)
    return result

# --- Test ---
test = '9 + 5 * 4'
calculate(test)
#there should be some more math tests




""" Task 3: Implement a Queue data structure from scratch, you can use array or list, or your linked list"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0)
    def poll(self):
        return self.items[0]
    def size(self):
        return len(self.items)
        


        




