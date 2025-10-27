""" Task-1: Implement a Hash data structure from scratch."""
import re

#Instructions to Run:
# in the vs code terminal, run this 
# $ cd .\SWE240P_DataStructures\
# then run the file 
# $  python .\HW3.py
# then select the text file to run
# $ pride-and-prejudice.txt

# ---------------------------- #
#  Custom Hash Map Data Structure
# ---------------------------- #
# Implements a hash table using separate chaining (lists for collisions)
# Uses polynomial rolling hash function
# Automatically resizes when load factor > 0.75

class Hashmap:
    # Time Complexity: O(n) — creates n empty lists
    # Space Complexity: O(n)
    def __init__(self):
        self.mod = 50
        self.buckets=[]
        for i in range(50):
            self.buckets.append([])


      
        
    
    # Time Complexity: O(n) — must reinsert every key
    # Space Complexity: O(n) — new list of buckets
    def resize(self):
       
        old_buckets = self.buckets
        new_capacity = len(self.buckets) *2
        self.mod = new_capacity
        new_buckets = [[] for _ in range(new_capacity)]
        
        self.capacity = new_capacity
        self.buckets = new_buckets  
        for bucket in old_buckets:
            for key in bucket:
                self.insert(key)

    # Average Time Complexity: O(1)
    # Worst-Case Time Complexity: O(n) if all keys hash to the same bucket
    # Space Complexity: O(1)
    def contains(self, word):
        index = self.hash(word)
        return word in self.buckets[index]

    #keygen function going on polynomial approach
    # Convert a string into an integer index using a polynomial rolling hash.
    # Time Complexity: O(m), where m = length of x
    # Space Complexity: O(1)
    def hash(self,x):
        base=33 # the textbook said this was a good number to use
        size=len(x)
        # turn the character into a number 0-25
        def chartoval(character: str) -> int:
            return ord(character) - ord('a') +1
        hashval = 0 
        #textbook said to use reversed for simpler exponent logic, could be done regular style also
        for c in reversed(x):
            #polynomial hashing formula from textbook
            hashval = (chartoval(c) + base * hashval)
            hashval = hashval % self.mod

        return(hashval)
    

    # Average Time Complexity: O(1)
    # Worst-Case Time Complexity: O(n) (rehashing entire table)
    # Space Complexity: O(1) amortized; O(n) during resize
    def insert(self,x:str):
        tolerance = self.size() / len(self.buckets)
        if tolerance > .75:
            print("Load factor exceeded 0.75, resizing...")
            self.resize()

        val = self.hash(x)
        self.buckets[val].append(x)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def size(self):
        total = 0
        for b in self.buckets:
           if b:
               total += len(b)
        return total
   
# Test Cases for task 1


"""Task 2"""
# parse through pride and prejudice line by line 

# Time complexity: O(t *m) where t is t is the total words proccesed and m is the word length
#Space complexity: O(t)
def processFile():
    print("Enter Filename")
    print("Please Use a .txt file in the same directory")


    filename = input()
    
    #edge cases, error messages here

    map = Hashmap()
    with open(filename, 'r') as f:
        for line in f:
            # Split line by non-alphanumeric characters
            words = re.split(r'[^a-zA-Z0-9]+', line.strip())

            for word in words:
                if word == "":
                    continue  # skip empty strings

                word = word.lower()
                word = sorted(word)
                word = "".join(word)

                if map.contains(word):
                    pass
                else:
                    map.insert(word)

        print(map.buckets)
    print(map.size())

    




processFile()
print

