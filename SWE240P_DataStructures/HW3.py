""" Task-1: Implement a Hash data structure from scratch."""



# HashTable: A fixed-size array or list. Depending on your hash function,
class Hashmap:
    def __init__(self):
        self.mod = 20
        self.buckets=[]
        for i in range(20):
            self.buckets.append([])

            

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

        print( hashval)

map = Hashmap()
map.hash('hi')




# Your hash function must have a collision-resolution mechanism.


# insert(x):  Insert string x to the HashTable in the index returned by hash(x).
# size():  Returns the size of the elements, i.e., the number of keys.