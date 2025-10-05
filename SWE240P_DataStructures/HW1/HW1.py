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

    def addUser(self,name,address,ss,balance):
        new_node = Node(name,address,ss,balance)

        if self.head == None:
            self.head = new_node
        else:
            #implement a checking function to see if the id is not current.id +1, if so theres a blank spot where the node should go
            #an edge case could be if the first node doesnt have a id, could be checked easily with "if head.id != 0"
            current=self.head
            while current.next is not None:
                # check to see if there is an empty space in between id's
                if current.next and current.next.id> current.id +1:
                    new_node.id = current.id +1
                    new_node.next = current.next
                    current.next = new_node
                    break
                    
        
                current = current.next
            current.next = new_node

    def deleteUser(self,id):
        current = self.head
        #if id is associated with head
        if current.id == id:
            self.head == current.next
            current.next = None

        else:
            while current.next.id != id:
                current = current.next
            toBeDeleted = current.next
            current.next = current.next.next
            toBeDeleted.next = None

# Task-4: Write a method/function 
# payUserToUser(payer ID, payee ID, amount) 
# that lets the user with ID1 pay the user with ID3 by amount.
    def payUserToUser(self,payerID,payeeID,amount):
        if payeeID == payerID:
            print("Cannot initiate transaction between the same account")

        current = LL.head
        completion_check = 0
        while current:
            
            if current.id == payeeID:
                payee = current
                completion_check +=1
            if current.id == payerID:
                payer = current
                completion_check +=1

            if completion_check == 2:
                break
            current = current.next


        if amount > payer.balance:
            print("The requested transaction could not be completed")
            print("The specified account does not have the required balance")
            return 
        payer.balance -= amount
        payee.balance += amount
        print("Transfer Complete")
        


            
            
            

        
















""" Test Cases"""

"Adding new user"
LL = LinkedList()
LL.addUser("flannigan","55 maple drive",135548399,50)
LL.addUser("flannigans brother ","77 maple drive",435335,50)
LL.addUser("flannigans OTHER  brother ","79 maple drive",135548393,90)
current = LL.head


while current:
    print(current.name,current.id, "-->")     
    current = current.next

print("Null")
print("---end of test---")

""" deleteuser"""
#add something in here to add a new user after one is deleted to make sure the open id is taken


LL.deleteUser(2)




current = LL.head


while current:
    print(current.name,current.id, "-->")
    current = current.next

print("Null")
LL.addUser("flannigans OTHER  brother ","79 maple drive",135548393,10000)
print("---end of test ---")


""" Task4-payUser-test"""
print("intiating a payment from user 0 to user 1")
current = LL.head
while current:
    print(current.id,"balance =",current.balance, "-->")
    current = current.next

print("Null")

print("after the payment is complete user 0 should have 25 dollars, and user 1 should have 75")
LL.payUserToUser(0,1,25)

current = LL.head
while current:
    print(current.id,"balance =",current.balance, "-->")
    current = current.next

print("Null")


# notes
#add something to verify ss number lengths, as well as avoid dupes in the list