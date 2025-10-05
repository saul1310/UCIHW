# Task Description:

# Consider a commercial bank, Bank of Orange County, where anyone can open bank accounts. To open a bank account, the following information is needed - 

# Name 
# Address
# Social Security
# An initial deposit amount. 
# The bank assigns a unique ID whenever a user opens an account. The unique ID is incrementally assigned to new users, meaning if the last new user’s ID is x, the user signing up will have a unique ID (x + 1). If a user closes their account, the unique ID can be re-claimed and re-assigned to future new users. 

# Now, write a class for the Bank of Orange County to complete the following tasks - 



# Task-1: Model the list of users as a linked list 
# where each account is a node in the list.
# Users must be sorted by their ID in the linked list. 

#  initialization of node class
class Node:
    _currentIDNum = 0
    def __init__(self,name,address,ss,balance,):
        self.name = name
        self.next = None
        self.address = address
        self.ss = ss
        self.balance = balance
        self.id = Node._currentIDNum
        Node._currentIDNum +=1

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self,name,address,ss,balance):
        new_node = Node(name,address,ss,balance)

        if self.head == None:
            self.head = new_node
        else:
            current=self.head
            while current.next is not None:
                current = current.next
            current.next = new_node












LL = LinkedList()
LL.add_node("flannigan","55 maple drive",135548399,10000)
LL.add_node("flannigans brother ","77 maple drive",135548398,10000)
current = LL.head

while current:
    print(current.name,current.id, "-->")
    current = current.next

print("Null")


""" Test Cases"""