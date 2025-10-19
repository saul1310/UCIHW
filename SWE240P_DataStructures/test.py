import re

# Step 1: Use Python's built-in dictionary as a hashmap
class TestHashMap:
    def __init__(self):
        self.map = {}

    def insert(self, key):
        if key not in self.map:
            self.map[key] = True  # Value doesn't matter

    def size(self):
        return len(self.map)

# Step 2: Function to process the file
def count_unique_anagram_roots(file_path):
    hashmap = TestHashMap()
    pattern = re.compile(r'[^a-zA-Z0-9]')  # delimiters: anything not alphanumeric
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split line into words using regex
            words = [w.lower() for w in pattern.split(line) if w]
            for word in words:
                # Sort characters to get anagram root
                anagram_root = ''.join(sorted(word))
                hashmap.insert(anagram_root)

    return hashmap.size()

# Step 3: Test with the file
file_path = 'pride-and-prejudice.txt'
unique_anagram_count = count_unique_anagram_roots(file_path)
print("Number of unique anagram roots:", unique_anagram_count)
