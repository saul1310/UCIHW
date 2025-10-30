from collections import deque
import sys
import os

#instructions to run:
# just run file

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
    # Time Complexity: O(n) -- visit each element once
    # Space Complexity: O(n) -- store a Node object for each element

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
    
    # Runtime Complexity: O(n log n) -- each insertion O(log n)
    # Space Complexity: O(n) -- heap array + tree nodes

    def createMaxHeap(self, values):
        """
        Takes a list of integers, creates a max heap, and returns it as a binary tree (Node root)
        """
        heap = self.MaxHeap()
        for val in values:
            heap.insert(val)
        return array_to_tree(heap.a)
    # Runtime Complexity: O(n log n)
    # Space Complexity: O(n)
    
  # ---------------- Task-2 Methods ----------------
class BSTToHeapTransformer:
    def bstToMinHeap(self, bst, heap):
        # helper dfs function
        def dfs(root):
            if not root:
                return
            heap.insert(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(bst.root)
        
    def bstToMaxHeap(self, bst, heap):
        # helper dfs function
        def dfs(root):
            if not root:
                return
            heap.insert(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(bst.root)


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

    # Runtime Complexity: O(n) -- visit each node once
    # Space Complexity: O(n) -- queue storage

# ---------------- Sample Test Suite ----------------
# ---------------- Enhanced Test Suite ----------------
def check_heap_property(root, min_heap=True):
    """
    Checks if the tree rooted at 'root' satisfies min-heap or max-heap property.
    Returns True/False.
    """
    if not root:
        return True
    left_ok = True
    right_ok = True
    if root.left:
        if min_heap:
            left_ok = root.val <= root.left.val
        else:
            left_ok = root.val >= root.left.val
        left_ok = left_ok and check_heap_property(root.left, min_heap)
    if root.right:
        if min_heap:
            right_ok = root.val <= root.right.val
        else:
            right_ok = root.val >= root.right.val
        right_ok = right_ok and check_heap_property(root.right, min_heap)
    return left_ok and right_ok


def run_full_tests():
    builder = HeapBuilder()
    transformer = BSTToHeapTransformer()

    # Task 1: HeapBuilder tests
    heap_test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [10, 20, 15, 30, 40, 5, 7],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [3, 3, 2, 1, 4, 4, 5],
        [],
        [42],
        [100, 50, 200, 25, 75, 150, 250]
    ]

    print("\n=== Task 1: HeapBuilder Tests ===")
    for idx, arr in enumerate(heap_test_cases, 1):
        print(f"\n--- Test {idx} ---")
        print(f"Input array: {arr}")

        # MinHeap
        min_heap_root = builder.createMinHeap(arr)
        print("Min Heap (level order):")
        print_tree_level_order(min_heap_root)
        root_check = min_heap_root.val == min(arr) if arr else True
        property_check = check_heap_property(min_heap_root, min_heap=True)
        print(f"Min Heap root correct? {root_check}")
        print(f"Min Heap property valid? {property_check}")

        # MaxHeap
        max_heap_root = builder.createMaxHeap(arr)
        print("Max Heap (level order):")
        print_tree_level_order(max_heap_root)
        root_check = max_heap_root.val == max(arr) if arr else True
        property_check = check_heap_property(max_heap_root, min_heap=False)
        print(f"Max Heap root correct? {root_check}")
        print(f"Max Heap property valid? {property_check}")

    # Task 2: BSTToHeapTransformer tests
    bst_test_cases = [
        [5, 3, 8, 1],
        [10, 5, 15, 3, 7, 12, 18],
        [2, 1, 3],
        [20, 10, 30, 5, 15, 25, 35],
        [1],  # single node
        []
    ]

    print("\n=== Task 2: BSTToHeapTransformer Tests ===")
    for idx, vals in enumerate(bst_test_cases, 1):
        print(f"\n--- Test {idx} ---")
        print(f"BST input values: {vals}")
        bst = IntBST()
        for v in vals:
            bst.insert(v)

        # MinHeap from BST
        minHeap = builder.MinHeap()
        transformer.bstToMinHeap(bst, minHeap)
        min_heap_root = array_to_tree(minHeap.getHeap())
        print("MinHeap from BST (level order):")
        print_tree_level_order(min_heap_root)
        root_check = min_heap_root.val == min(vals) if vals else True
        property_check = check_heap_property(min_heap_root, min_heap=True)
        print(f"Min Heap root correct? {root_check}")
        print(f"Min Heap property valid? {property_check}")

        # MaxHeap from BST
        maxHeap = builder.MaxHeap()
        transformer.bstToMaxHeap(bst, maxHeap)
        max_heap_root = array_to_tree(maxHeap.getHeap())
        print("MaxHeap from BST (level order):")
        print_tree_level_order(max_heap_root)
        root_check = max_heap_root.val == max(vals) if vals else True
        property_check = check_heap_property(max_heap_root, min_heap=False)
        print(f"Max Heap root correct? {root_check}")
        print(f"Max Heap property valid? {property_check}")

    def test_bst_to_heap():
    # Create BST
        bst = IntBST()
        values = [10, 5, 15, 3, 7, 12, 18]  # example BST
        for v in values:
            bst.insert(v)

        print("Original BST (level order):")
        print_tree_level_order(bst.root)

        # Transform BST to MinHeap
        minHeapObj = HeapBuilder.MinHeap()
        transformer = BSTToHeapTransformer()
        transformer.bstToMinHeap(bst, minHeapObj)
        minHeapRoot = array_to_tree(minHeapObj.getHeap())

        print("\nMinHeap from BST (level order):")
        print_tree_level_order(minHeapRoot)
        print(f"Min Heap root correct? {minHeapRoot.val == min(values)}")
        print(f"Min Heap property valid? {check_heap_property(minHeapRoot, min_heap=True)}")

        # Transform BST to MaxHeap
        maxHeapObj = HeapBuilder.MaxHeap()
        transformer.bstToMaxHeap(bst, maxHeapObj)
        maxHeapRoot = array_to_tree(maxHeapObj.getHeap())

        print("\nMaxHeap from BST (level order):")
        print_tree_level_order(maxHeapRoot)
        print(f"Max Heap root correct? {maxHeapRoot.val == max(values)}")
        print(f"Max Heap property valid? {check_heap_property(maxHeapRoot, min_heap=False)}")

    test_bst_to_heap()

# ---------------- Run Enhanced Tests ----------------
if __name__ == "__main__":
    run_full_tests()