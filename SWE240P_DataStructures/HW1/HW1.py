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
    """A node representing a bank account.

    Class variables:
    - _currentIDNum: next sequential id to assign when no reclaimed ids.
    - _free_ids: min-heap of reclaimed ids available for reuse.
    """
    _currentIDNum = 0
    _free_ids = []

    def __init__(self, name, address, ss, balance, id=None):
        """Create a node. If `id` provided, use it; otherwise allocate a new id.

        The optional `id` parameter is used when reusing an id from the
        reclaimed pool or when intentionally creating a node with a specific id
        (used by mergeBanks).
        """
        self.name = name
        self.next = None
        self.address = address
        self.ss = ss
        self.balance = balance
        if id is not None:
            # Use a supplied id (reused or forced)
            self.id = id
        else:
            # Allocate next sequential id
            self.id = Node._currentIDNum
            Node._currentIDNum += 1


class LinkedList:
    def __init__(self):
        self.head = None

    def addUser(self, name, address, ss, balance):
        """Add a new user and keep the linked list ordered by id.

        Reuse the smallest reclaimed id if available (pop from min-heap). The
        function returns the assigned id so callers/tests can use the actual id
        (important because ids might be reused and not always sequential).
        """
        if Node._free_ids:
            # Reuse smallest available reclaimed id
            id_to_use = heapq.heappop(Node._free_ids)
            new_node = Node(name, address, ss, balance, id=id_to_use)
        else:
            # Allocate a fresh sequential id
            new_node = Node(name, address, ss, balance)

        if self.head is None:
            self.head = new_node
            return new_node.id

        if new_node.id < self.head.id:
            new_node.next = self.head
            self.head = new_node
            return new_node.id

        current = self.head
        while current.next is not None and current.next.id < new_node.id:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return new_node.id

    def deleteUser(self, id):
        current = self.head
        # Standard linked-list delete. On successful delete push the freed id
        # into the reclaimed-id min-heap so it may be reused by future addUser
        if current is None:
            print("List is empty.")
            return

        if current.id == id:
            self.head = current.next
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
        # Reclaim the id for reuse
        heapq.heappush(Node._free_ids, toBeDeleted.id)
        toBeDeleted.next = None

    def payUserToUser(self, payerID, payeeID, amount):
        """Transfer amount from payer to payee.

        Looks up both accounts in a single traversal. Prints messages and
        returns early if accounts are missing or payer has insufficient funds.
        """
        if payeeID == payerID:
            print("Cannot initiate transaction between the same account")
            return

        current = self.head
        payer = None
        payee = None
        while current:
            if current.id == payeeID:
                payee = current
            if current.id == payerID:
                payer = current
            if payer and payee:
                break
            current = current.next

        if not payer or not payee:
            print("One or both accounts not found.")
            return

        if amount > payer.balance:
            print("The requested transaction could not be completed")
            print("The specified account does not have the required balance")
            return

        payer.balance -= amount
        payee.balance += amount
        print("Transfer Complete")

    def getMedianID(self):
        """Return the median id in the list.

        If the list length is even this returns the average of the two
        middle ids; if odd it returns the middle id. Returns None on empty
        list.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if count == 0:
            return None
        # For even count, we want the two middle elements at indexes
        # (count//2 - 1) and (count//2). For odd count, we want the element
        # at index count//2. Using zero-based indexing, compute the index of
        # the lower-middle element and advance to it.
        lower_middle = (count - 1) // 2
        current = self.head
        for i in range(lower_middle):
            current = current.next
        if count % 2 == 0:
            return (current.id + current.next.id) / 2
        else:
            return current.id

    def mergeAccounts(self, ID1, ID2):
        """Merge two accounts if their name/address/ss match.

        The account with the smaller id is kept and the other is deleted; the
        kept account's balance increases by the deleted account's balance.
        """
        if ID1 == ID2:
            print("Cannot merge the same account")
            return
        current = self.head
        account1 = None
        account2 = None
        while current:
            if ID1 == current.id:
                account1 = current
            if ID2 == current.id:
                account2 = current
            current = current.next
        if not account1 or not account2:
            print("One or both accounts not found.")
            return
        if account1.name == account2.name and account1.address == account2.address and account1.ss == account2.ss:
            toKeep = account1 if account1.id < account2.id else account2
            toDelete = account2 if toKeep is account1 else account1
            toKeep.balance += toDelete.balance
            self.deleteUser(toDelete.id)
            print(f"Accounts {ID1} and {ID2} merged successfully into ID {toKeep.id}.")
        else:
            print("unable to merge accounts")

    @staticmethod
    def mergeBanks(bankOfOrangeCounty, bankOfLosAngeles):
        """Merge two banks into a new LinkedList.

        This preserves account data and attempts to preserve ids; when an id
        collision is detected the smallest available reclaimed id is used or a
        new sequential id is assigned. addUser is used to insert nodes and the
        assigned id is then forced to the desired value by walking to the tail
        and setting current.id (this keeps addUser's validation and ordering
        logic while ensuring the merged id set matches the desired values).
        """
        mergedBank = LinkedList()
        used_ids = set()

        def add_node_to_merged(node):
            # Choose a new id if node.id already used in mergedBank
            if node.id in used_ids:
                if Node._free_ids:
                    new_id = heapq.heappop(Node._free_ids)
                else:
                    new_id = Node._currentIDNum
                    Node._currentIDNum += 1
            else:
                new_id = node.id

            used_ids.add(new_id)

            # Insert a copy via addUser (preserves list invariants)
            mergedBank.addUser(node.name, node.address, node.ss, node.balance)

            # Force the intended id on the newly added tail node. This is a
            # small, explicit step after insertion to ensure mergedBank contains
            # the id we selected above.
            current = mergedBank.head
            while current.next:
                current = current.next
            current.id = new_id

        current = bankOfOrangeCounty.head
        while current:
            add_node_to_merged(current)
            current = current.next

        current = bankOfLosAngeles.head
        while current:
            add_node_to_merged(current)
            current = current.next

        print("Banks merged successfully into Bank of Southern California.")
        return mergedBank


""" TEST CASES"""


def print_bank(bank: LinkedList, title: str) -> None:
    print(f"\n{title}")
    current = bank.head
    if not current:
        print("  <empty>")
    while current:
        print(f"  ID={current.id}, Name={current.name}, Address={current.address}, SS={current.ss}, Balance={current.balance}")
        current = current.next
    print("  Null")


def print_header(test_name: str) -> None:
    print('\n' + '=' * 60)
    print(f"TEST: {test_name}")
    print('-' * 60)


def test_add_delete_reuse():
    print_header('add_delete_reuse')
    bank = LinkedList()
    id1 = bank.addUser("flannigan", "55 maple drive", 135548399, 50)
    id2 = bank.addUser("flannigans brother", "77 maple drive", 435335, 50)
    id3 = bank.addUser("flannigans OTHER brother", "79 maple drive", 135548393, 90)

    print_bank(bank, "Test: add users (initial)")

    print(f"\nDeleting user with ID={id3}")
    bank.deleteUser(id3)
    print_bank(bank, "After deletion")

    print("\nAdding a new user (should reuse reclaimed id if available)")
    new_id = bank.addUser("new member", "100 Oak St", 555666777, 10000)
    print(f"Added new user with assigned ID={new_id}")
    print_bank(bank, "After adding new user")


def test_pay():
    print_header('payUserToUser')
    bank = LinkedList()
    id0 = bank.addUser("payer", "Addr0", 111111111, 50)
    id1 = bank.addUser("payee", "Addr1", 222222222, 50)

    print_bank(bank, "Test: payUserToUser - before")
    print(f"\nTransferring 25 from ID={id0} to ID={id1}")
    bank.payUserToUser(id0, id1, 25)
    print_bank(bank, "Test: payUserToUser - after")


def test_median():
    print_header('median')
    bank = LinkedList()
    for i in range(7):
        bank.addUser(f"user{i}", f"address{i}", 111111110 + i, 10)

    print_bank(bank, "Test: median - list")
    median = bank.getMedianID()
    print(f"Median id is: {median}")


def test_merge_accounts():
    print_header('merge_accounts')
    bank = LinkedList()
    id_a1 = bank.addUser("Alice", "123 Main St", 999111222, 50)
    id_a2 = bank.addUser("Alice", "123 Main St", 999111222, 100)
    id_b = bank.addUser("Bob", "999 Elm St", 888777666, 200)

    print_bank(bank, "Test: mergeAccounts - before")

    print(f"\nMerging accounts {id_a1} and {id_a2} (should succeed)")
    bank.mergeAccounts(id_a1, id_a2)
    print_bank(bank, "After successful merge")

    print(f"\nAttempting to merge {id_a1} and {id_b} (should fail)")
    bank.mergeAccounts(id_a1, id_b)
    print_bank(bank, "After failed merge attempt")


def test_merge_banks():
    print_header('merge_banks')
    boc = LinkedList()
    id_boc_a = boc.addUser("Alice", "123 Main St", 111111111, 100)
    id_boc_b = boc.addUser("Bob", "456 Elm St", 222222222, 200)

    bla = LinkedList()
    id_bla_c = bla.addUser("Charlie", "789 Pine St", 333333333, 300)
    id_bla_b = bla.addUser("Bob", "456 Elm St", 222222222, 150)

    if bla.head:
        bla.head.id = id_boc_b

    print_bank(boc, "Bank of Orange County (before merge)")
    print_bank(bla, "Bank of Los Angeles (before merge)")

    merged = LinkedList.mergeBanks(boc, bla)
    print_bank(merged, "Merged Bank of Southern California (after merge)")


if __name__ == "__main__":
    test_add_delete_reuse()
    test_pay()
    test_median()
    test_merge_accounts()
    test_merge_banks()
