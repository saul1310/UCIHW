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
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ------------------ BST Class ------------------
class BST:
    def __init__(self):
        self.root = None

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

    def inorder_to_file(self, filename):
        with open(filename, "w") as f:
            def _inorder(node):
                if node:
                    _inorder(node.left)
                    f.write(str(node.data) + "\n")
                    _inorder(node.right)
            _inorder(self.root)

# ------------------ Build BST from File ------------------
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
                # delete method would go here
                pass

            # Debug print to confirm it's reading correctly
            # print(f"Read: {current}")
    return bst


# ------------------ Run ------------------
filename = input("Enter filename: ")
tree = build_bst_from_file(filename)
tree.inorder_to_file("output.txt")
