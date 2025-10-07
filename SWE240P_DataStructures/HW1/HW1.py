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
import heapq

class Node:
    _currentIDNum = 0
    # min-heap of reclaimed ids available for reuse
    _free_ids = []

    def __init__(self, name, address, ss, balance, id=None):
        self.name = name
        self.next = None
        self.address = address
        self.ss = ss
        self.balance = balance
        # If an id is provided (reused), take it. Otherwise allocate a new id.
        if id is not None:
            self.id = id
        else:
            self.id = Node._currentIDNum
            Node._currentIDNum += 1

class LinkedList:
    def __init__(self):
        self.head = None

    def addUser(self,name,address,ss,balance):
       
        if Node._free_ids:
            id_to_use = heapq.heappop(Node._free_ids)
            new_node = Node(name, address, ss, balance, id=id_to_use)
        else:
            new_node = Node(name, address, ss, balance)

        # insert into the linked list while maintaining order by id
        if self.head is None:
            self.head = new_node
            return

        # if new node should become new head
        if new_node.id < self.head.id:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.id < new_node.id:
            current = current.next

        # insert after current
        new_node.next = current.next
        current.next = new_node

    def deleteUser(self, id):
        current = self.head
        
   
        if current is None:
            print("List is empty.")
            return

        #
        if current.id == id:
            self.head = current.next
            # reclaim the id
            heapq.heappush(Node._free_ids, current.id)
            current.next = None
            return

       
        while current.next is not None and current.next.id != id:
            current = current.next

   
        if current.next is None:
            print("User not found.")
            return

     
        toBeDeleted = current.next
        current.next = toBeDeleted.next
        # reclaim the id from the deleted node so it can be reused
        heapq.heappush(Node._free_ids, toBeDeleted.id)
        toBeDeleted.next = None


    def payUserToUser(self,payerID,payeeID,amount):
        if payeeID == payerID:
            print("Cannot initiate transaction between the same account")

        current = self.head
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

    def getMedianID(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.next
        median_index = count//2
        current = self.head
        for i in range(median_index):
            current = current.next
        if count %2 ==0:
            return (current.id + current.next.id)/2
        else:
            return current.id
        


            
            
            

        
















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

print("---end of test---")

""" Task5-median test"""

print("deleting all nodes and adding new ones to test median function")

while LL.head:
    LL.deleteUser(LL.head.id)  
print("nodes deleted") 


LL = LinkedList()

LL.addUser("user0","address0",111111111,10)
LL.addUser("user1","address1",111111112,10)
LL.addUser("user2","address2",111111113,10)
LL.addUser("user3","address3",111111114,10)
LL.addUser("user4","address4",111111115,10)
LL.addUser("user5","address5",111111116,10)
LL.addUser("user6","address6",111111117,10)
current = LL.head
while current:
    print(current.id,"balance =",current.balance, "-->")
    current = current.next

print("Null")


""" Task5-median test"""
print("median id is:",LL.getMedianID())


# notes
#add something to verify ss number lengths, as well as avoid dupes in the list