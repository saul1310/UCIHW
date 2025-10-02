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

class Node:
    _currentIDNum = 0
    def __init__(self,name,address,ss,balance,id):
        self.name = name
        self.next = None
        self.address = address
        self.ss = ss
        self.balance = balance
        self.id = Node._currentIDNum
        Node._currentIDNum +=1

def uniqueid():


node1 = Node(15)
node2 = Node(3)
node3 = Node(234)

node1.next = node2
node2.next = node3

head = node1

current = head
while current:
    print(current.data, "-->")
    current = current.next

print("Null")
