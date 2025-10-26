from collections import deque
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from HW4.HW4 import IntBST


# ---------------- Node Class ----------------
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ---------------- Helper Function ----------------
def array_to_tree(arr):
    """
    Converts a heap stored in an array into a binary tree of Node objects.
    """
    if not arr:
        return None
    nodes = [Node(val) for val in arr]
    for i in range(len(arr)):
        left_index = 2*i + 1
        right_index = 2*i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    return nodes[0]  # return root

# ---------------- HeapBuilder Class ----------------
class HeapBuilder:
    class MinHeap:
        def __init__(self):
            self.a = []

        """Insert a new element into the minheap"""
        # Time complexity: O(n log n) --> when ran on a entire array
        # Space complexity : O(n)
        def insert(self, val):
            self.a.append(val)
            i = len(self.a) - 1
            # i starts at the bottom of the heap, and bubbles up, comparing the inserted val
            # with every element until the right location is found ie, the parent is smaller than val
            while i > 0 and self.a[(i-1)//2] > self.a[i]:
                # until the condition is met, continue swapping upward
                self.a[i], self.a[(i-1)//2] = self.a[(i-1)//2], self.a[i]
                # move i upward (closer to the 0th element, the root)
                # our tracker for val is assigned to the parent, since val and the parent just switched
                i = (i-1)//2

        """Print the heap: for testing"""
        def printheap(self):
            print("Min Heap:", self.a)

        """Return the heap: for testing"""
        def getHeap(self):
            return self.a

    class MaxHeap:
        def __init__(self):
            self.a = []

        """Insert a new element into the maxheap"""
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        def insert(self, val):
            # insert new val at the bottom of the heap, and bubbles it up comparing the inserted val
            # with every element until the right location is found, ie, the parent is larger than val
            self.a.append(val)
            i = len(self.a) - 1
            while i > 0 and self.a[(i-1)//2] < self.a[i]:
                # until the condition is met, continue swapping upward
                self.a[i], self.a[(i-1)//2] = self.a[(i-1)//2], self.a[i]
                # our tracker for val is assigned to the parent, since val and the parent just switched
                i = (i-1)//2

        """Print the heap: for testing"""
        def printheap(self):
            print("Max Heap:", self.a)

        """Return the heap: for testing"""
        def getHeap(self):
            return self.a

    # ---------------- Task-1 Methods ----------------
    def createMinHeap(self, values):
        """
        Takes a list of integers, creates a min heap, and returns it as a binary tree (Node root)
        """
        heap = self.MinHeap()
        for val in values:
            heap.insert(val)
        return array_to_tree(heap.a)

    def createMaxHeap(self, values):
        """
        Takes a list of integers, creates a max heap, and returns it as a binary tree (Node root)
        """
        heap = self.MaxHeap()
        for val in values:
            heap.insert(val)
        return array_to_tree(heap.a)
    
      # ---------------- Task-2 Methods ----------------
    class BSTToHeapTransformer:
        def bstToMinHeap(self,bst,heap):
            #helper dfs function
            def dfs(root):
                if not root:
                    return
                heap.insert(root.val)
                
                 
                dfs(root.right)
                dfs(root.left)
      


            
        def bstToMaxHeap(self,bst):
            pass
    

    


# ---------------- Testing Utilities ----------------
def print_tree_level_order(root):
    """
    Prints the binary tree level by level (useful for testing maybe who knows)
    """
    if not root:
        print("Empty tree")
        return
    q = deque([root])
    result = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    for idx, lvl in enumerate(result):
        print(f"Level {idx}: {lvl}")

# ---------------- Sample Test Suite ----------------
def test_heaps():
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 20, 15, 30, 40],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [3, 3, 2, 1, 4, 4, 5],
    ]

    builder = HeapBuilder()

    for idx, arr in enumerate(test_cases, 1):
        print(f"\n--- Test {idx} ---")
        print(f"Input array: {arr}")

        # Expected results (for comparison purposes)
        expected_min = sorted(arr)
        expected_max = sorted(arr, reverse=True)

        # -------- MinHeap --------
        min_heap_root = builder.createMinHeap(arr)
        print("Min Heap (level order):")
        print_tree_level_order(min_heap_root)
        # Root check
        print(f"Min Heap root correct? {'Yes' if min_heap_root.val == min(arr) else 'No'}")

        # -------- MaxHeap --------
        max_heap_root = builder.createMaxHeap(arr)
        print("Max Heap (level order):")
        print_tree_level_order(max_heap_root)
        # Root check
        print(f"Max Heap root correct? {'Yes' if max_heap_root.val == max(arr) else 'No'}")


# ---------------- Run Tests ----------------
# if __name__ == "__main__":
#     test_heaps()
bst = IntBST()
for val in [5, 3, 8, 1]:
    bst.insert(val)

root = bst.root
bst.print_level_order()