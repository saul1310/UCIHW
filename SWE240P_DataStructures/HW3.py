""" Task-1: Implement a Hash data structure from scratch."""
import re


# HashTable: A fixed-size array or list. Depending on your hash function,
#should this have the size as a parameter you can define?
class Hashmap:
    def __init__(self):
        self.mod = 50
        self.buckets=[]
        for i in range(50):
            self.buckets.append([])

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

            
    def contains(self, word):
        index = self.hash(word)
        return word in self.buckets[index]

    #keygen function going on polynomial approach
    def hash(self,x):
        base=33
        size=len(x)
        # turn the character into a number 0-25
        def chartoval(character: str) -> int:
            return ord(character) - ord('a') +1
        hashval = 0
        for c in reversed(x):
            hashval = (chartoval(c) + base * hashval)
            hashval = hashval % self.mod

        return(hashval)

    def insert(self,x:str):
        tolerance = self.size() / len(self.buckets)
        if tolerance > .75:
            print("Load factor exceeded 0.75, resizing...")
            self.resize()

        val = self.hash(x)
        self.buckets[val].append(x)

    def size(self):
        total = 0
        for b in self.buckets:
           if b:
               total += len(b)
        return total
   
# Test Cases for task 1


"""Task 2"""
# parse through pride and prejudice line by line 
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

