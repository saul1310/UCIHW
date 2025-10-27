import collections
from collections import deque

# ------------------ Student Class ------------------
class Student:
    def __init__(self, Studentnumber, LastName, Department, Program, Year):
        self.Studentnumber = Studentnumber
        self.LastName = LastName
        self.Department = Department
        self.Program = Program
        self.Year = Year

    def __str__(self):
        return f"{self.Studentnumber} {self.LastName} {self.Department} {self.Program} {self.Year}"


# ------------------ Node Class ------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ------------------ BST Class ------------------
# Time Complexity: O(1)
# Space Complexity: O(1)
class BST:
    def __init__(self):
        self.root = None
    
    #Iterates through the tree, once it find the missing spot where 
    # the new node should be it creates a node object with the student info 
    #Time Complexity: O(n) in worst case if tree unbalanced
    # Space Complexity: O(h) recursion depth
    def insert(self, student):
        def _insert(root, student):
            if not root:
                return Node(student)
            if student.LastName.lower() < root.data.LastName.lower():
                root.left = _insert(root.left, student)
            elif student.LastName.lower() > root.data.LastName.lower():
                root.right = _insert(root.right, student)
            return root
        self.root = _insert(self.root, student)

    # Time complexity: O(n), searchng for node
    # space: O(h) for recursion stack
    def delete(self, last_name):
        def _delete(root, last_name):
            if not root:
                return None
            if last_name.lower() < root.data.LastName.lower():
                root.left = _delete(root.left, last_name)
            elif last_name.lower() > root.data.LastName.lower():
                root.right = _delete(root.right, last_name)
            else:
                # Case 1: No child
                if not root.left and not root.right:
                    return None
                # Case 2: One child
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                # Case 3: Two children
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.data = successor.data
                root.right = _delete(root.right, successor.data.LastName)
            return root
        self.root = _delete(self.root, last_name)


    #DFS Traversal, and prints each nodes data to a text file
    # Time Complexity: O(n) (visits each node once)
    # Space Complexity:  (O(n) worst-case if skewed)
    def inorder_to_file(self, filename):
        with open(filename, "w") as f:
            def _inorder(node):
                if node:
                    _inorder(node.left)
                    f.write(str(node.data) + "\n")
                    _inorder(node.right)
            _inorder(self.root)

    """ Prints the BST level by level."""
    #BFS method
    #time complexity: O(n)
    # Space Complexity: O(n)
    def print_bst_level_order(root):
  
        if not root:
            print("Empty BST")
            return
        q = deque([root])
        while q:
            level_size = len(q)
            level_vals = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val if hasattr(node, "val") else node.data)  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            print(level_vals)

    def get_bst_root(bst):
        return bst.root
                
    def inorder_to_fileBFS(self, filename):
        if not self.root:
            return

        with open(filename, "w") as f:
            q = collections.deque()
            q.append(self.root)

            while q:
                node = q.popleft()
                if node:
                    # Write the string representation of the Student to the file
                    f.write(str(node.data) + "\n")
                    # Add children to the queue
                    q.append(node.left)
                    q.append(node.right)


              


    #BFS Traversal, and prints each nodes data to a text file

# ------------------ Build BST from File ------------------
# time complexity: O(m * n) where m is num of lines and n is elements
# space complexity: o(n), num of bst nodes
def build_bst_from_file(filename):
    bst = BST()
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            op = line[0]
            student_number = line[1:8]
            last_name = line[8:33].strip()
            department = line[33:37]
            program = line[37:41]
            year = line[41]

            current = Student(student_number, last_name, department, program, year)

            if op == 'I':
                bst.insert(current)
            elif op == 'D':
                bst.delete(current)

            # Debug print to confirm it's reading correctly
            # print(f"Read: {current}")
    return bst

class IntBST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            
    # time complexity: o(n)
    # space: o(n)
    def insert(self, val):
        def _insert(root, val):
            if not root:
                return self.Node(val)
            if val < root.val:
                root.left = _insert(root.left, val)
            elif val > root.val:
                root.right = _insert(root.right, val)
            return root
        self.root = _insert(self.root, val)

    # time complexity:o(n)
    # space: o(n)
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.val)
                _inorder(node.right)
        _inorder(self.root)
        return result


# ------------------ Run ------------------
if __name__ == "__main__":
    filename = input("Enter filename: ")
    tree = build_bst_from_file(filename)
    tree.inorder_to_fileBFS("output.txt")

    #dfs and bfs test
    test_filename = "dfs_bfs_info.txt"
    with open(test_filename, "w") as f:
        f.write("I8534534McKay                    0251CT  1\n")
        f.write("I8400342LaPorte                  0045JA  1\n")
        f.write("I8499120Black                    0341RST 1\n")
        f.write("I8400912Green                    0045RFM 1\n")
        f.write("I8212399Schafer                  0251EST 1\n")

    # Build the BST from that file
    bst = build_bst_from_file(test_filename)

    # Write DFS traversal to file
    bst.inorder_to_file("dfs_output.txt")

    # Write BFS traversal to file
    bst.inorder_to_fileBFS("bfs_output.txt")

    print("BST built successfully.")
    print("DFS output written to dfs_output.txt")
    print("BFS output written to bfs_output.txt")
