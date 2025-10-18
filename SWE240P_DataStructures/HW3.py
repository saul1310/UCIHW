""" Task-1: Implement a Hash data structure from scratch."""



# HashTable: A fixed-size array or list. Depending on your hash function,
#should this have the size as a parameter you can define?
class Hashmap:
    def __init__(self):
        self.mod = 5
        self.buckets=[]
        for i in range(5):
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

            

    #generate a key based on input
    #polynomial method
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
    # make a seen map using hashmap implementation
    with open(filename,'r') as f:
        for line in f:
            print(line)
    

# calculate the anagramrootword for each word

# insert word into map. if its present, skip it

#call the size function of the hash



# return number of unique words by calling size function
        





print("Creating Hashmap with initial capacity 5")
map = Hashmap()
words_to_insert = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon"
]

print("\nInserting words one by one:")
for word in words_to_insert:
    map.insert(word)
    print(f"Buckets after inserting", map.buckets)

print(f"Final size of hashmap: {map.size()}")
print(f"Final buckets count: {len(map.buckets)}")
print("Final buckets content:")
for i, bucket in enumerate(map.buckets):
    print(f"Bucket {i}: {bucket}")





# Your hash function must have a collision-resolution mechanism.


# insert(x):  Insert string x to the HashTable in the index returned by hash(x).
# size():  Returns the size of the elements, i.e., the number of keys.