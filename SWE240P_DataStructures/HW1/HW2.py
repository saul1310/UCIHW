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
        stck = Stack()
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
    eval_stack = Stack()
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

# (no immediate tests here) - tests are appended at end of file




""" Task 3: Implement a Queue data structure from scratch, you can use array or list, or your linked list"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0) if self.items else None
    def poll(self):
        return self.items[0] if self.items else None
    def size(self):
        return len(self.items)
        
""" Task 4: Implement a Stack using only two instances of the Queue class, write test cases to validate functionality."""


        

class StackWithTwoQs:
    def __init__(self):
        self.queueOne = Queue() 
        self.queueTwo = Queue()  
        pass

    def push(self, x):
        # Move all elements from queueOne to queueTwo
        while self.queueOne.size() > 0:
            self.queueTwo.enqueue(self.queueOne.dequeue())

        # Add the new element to queueOne
        self.queueOne.enqueue(x)

        # Move everything back to queueOne
        while self.queueTwo.size() > 0:
            self.queueOne.enqueue(self.queueTwo.dequeue())

    def pop(self):
        return self.queueOne.dequeue()

    def peek(self):
        return self.queueOne.poll()

    def size(self):
        return self.queueOne.size()

  

def _serialize_stack(s: Stack):
    # produce list snapshot
    return list(s.items)


def _print_test(name, before, after, expected):
    print('\n1: Name of test:', name)
    print('2: before input:', before)
    print('3: input after test has been done:', after)
    print('4: expected input:', expected)
    print('5: check if result matches expected input:', after == expected)


if __name__ == '__main__':
    # Test Stack
    st = Stack()
    before = _serialize_stack(st)
    st.push(1); st.push(2); st.push(3)
    after = _serialize_stack(st)
    expected = [1,2,3]
    _print_test('Stack push', before, after, expected)

    before = _serialize_stack(st)
    top = st.pop()
    after = _serialize_stack(st)
    expected = [1,2]
    _print_test('Stack pop', before, after, expected)

    # Test peek
    before = _serialize_stack(st)
    p = st.peek()
    after = _serialize_stack(st)
    expected = before
    _print_test('Stack peek (no mutation)', before, after, expected)

    # Test calculate
    expr = '9 + 5 * 4'
    before_calc = expr
    result = calculate(expr)
    after_calc = result
    expected_calc = 29.0
    _print_test('calculate simple expression', before_calc, after_calc, expected_calc)

    # Test Queue
    q = Queue()
    before = []
    q.enqueue('a'); q.enqueue('b')
    after = q.items.copy()
    expected = ['a','b']
    _print_test('Queue enqueue', before, after, expected)

    before = q.items.copy()
    popped = q.dequeue()
    after = q.items.copy()
    expected = ['b']
    _print_test('Queue dequeue', before, after, expected)

    # Test StackWithTwoQs
    sq = StackWithTwoQs()
    before = []
    sq.push(10); sq.push(20); sq.push(30)
    after = []
    # capture internal queueOne snapshot
    cur = []
    qtmp = sq.queueOne.items.copy()
    after = qtmp
    expected = [30,20,10]
    _print_test('StackWithTwoQs push (order)', before, after, expected)

    before = sq.queueOne.items.copy()
    popped = sq.pop()
    after = sq.queueOne.items.copy()
    expected = [20,10]
    _print_test('StackWithTwoQs pop', before, after, expected)



