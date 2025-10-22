# You are given an input ASCII text file containing an arbitrary number of student records in the following format:
# Operation code: 1 character ('I' for insert, 'D' for delete)
# Student number: 7 characters
# Student last name: 25 characters
# Home department: 4 characters
# Program: 4 characters
# Year: 1 character
# Each record is stored as one line in the text file; i.e., there is a newline character immediately following the year.

# Task 1: Build the BST

#create class for student info
class Student:
    def __init__(self,Studentnumber,LastName,Department,Program,Year):
        self.Studentnumber = ''
        self.LastName = ''
        self.Department = ''
        self.Program = ''
        self.year=''


# Node class for BST
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root= None



        

    def insert(self,Student):
        def _insert(Root,Student):
       
            if Root == None:
                return Node(Student)
            if Student.LastName.lower() < Root.Data.LastName.lower():
                Root.left = _insert(Root.left,Student)
            elif Student.LastName.lower > Root.Data.LastName.lower():
                Root.right = _insert(Root.right,Student)
            else:
                if Student.Studentnumber < Root.Data.Studnetnumber:
                    Root.left = _insert(Root.left,Student)
                else:
                    Root.right = _insert(Root.right,Student)
            self.Root = _insert(self.Root,Student)
      
        
def build_bst_from_file(filename):
        bst = BST
        with open(filename,"r") as file:
            for line in file:
                print(line)


var = input()
build_bst_from_file(var)