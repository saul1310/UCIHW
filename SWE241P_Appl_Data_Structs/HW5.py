# Task Description: Complete the following tasks.

# Task-1:  Given two strings s1 and s2, return true if s2 contains a permutation of s1, or 
# false otherwise.
#  In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"

# Output: true

# Explanation: s2 contains one permutation of s1 ("ba").

from collections import Counter


# Time complexity:
# O(len1+len2), or O(n)
#space Complexity:
# O(1), only constant operatoins used
def checkInclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False
    #Counter returns a dict freq map
    count1 = Counter(s1)
    window = Counter(s2[:len1])

    if count1 == window:
        return True
    #iterate through the length of s2
    for i in range(len1, len2):
        #i is at one character to the right of the string so we increase/ add it to the map by 1 count
        window[s2[i]] += 1
        #since weve moved right we need to decrement the character we left behind from our map
        window[s2[i - len1]] -= 1
        #if that recently decremented char now has a count of 0 remove it from the map
        if window[s2[i - len1]] == 0:
            del window[s2[i - len1]]
        #if our mao contains the same frequency as s1f, we have a match
        if count1 == window:
            return True

    return False



# Task-2:  You are given a chess board (of 8×8 dimension), and there are 8 queens placed randomly on the board. Each of the 8 queens is in different columns, and that means no two queens are attacking each other vertically. But some queens are attacking each other horizontally and/or diagonally. You have to move the queens so that no two queens are attacking each other from any direction. You are allowed to move the queens vertically, and thus, you can only change the row positions of each queen and not the column. A move consists of moving a queen from (R1, C) to (R2, C) where 1 ≤ R1, R2 ≤ 8 and R1 ̸= R2. You have to find the minimum number of moves required to complete the task.

# Each input consists of a line containing 8 integers. All these integers will be in the range [1, 8]. The i-th integer indicates the row position of a queen in the i-th column.

# Example 1: 

# Input: 1 2 3 4 5 6 7 8

# Output: 7

# Example 2:

# Input: 1 1 1 1 1 1 1 1

# Output: 7

# Write sample test cases to validate your implementation.

def is_valid(board, row, col):
    # Time Complexity: O(col) → we check all previous columns
    # Space Complexity: O(1) → only a few variables used
    for c in range(col):
        #if board[c] == row theres already a queen in the same row
        #if abs(board[c] - row) == abs(c - col) --> theres a queen on the same diagonal
        if board[c] == row or abs(board[c] - row) == abs(c - col):
            return False
    return True

def generate_solutions(col=0, board=None, solutions=None):
    # Time Complexity: O(92 * 8) = O(1) because there are exactly 92 valid 8-queen solutions.
    # Space Complexity: O(92*8) = O(1) storing all 92 solutions of length 8.

    #defualt paramters, when the function is initially called, this sets up our parameters:
    #board is set to [0,0,0,0,0,0,0,0], empty
    #solutions is initialized as an empty list for now
    if board is None:
        board = [0] * 8
    if solutions is None:
        solutions = []
    #our base case, if weve placed queens in all 8 columns, we have a complete board!
    if col == 8:
        #we then append our completed board to solutions, and return it
        #we append a shallow copy since were gonna keep using board
        solutions.append(board[:])
        return solutions
    #here we try each row for our current column, and check if its valid, if so we add it.
    for row in range(1, 9):  # rows 1 to 8
        if is_valid(board, row, col):
            board[col] = row
            #recursive fuinction: col = column we are currently trying to place a queen in
            #board  = current partial solution, list where we store the row pos of each queen
            #soluitons = a list of all valid solutions found so far
            generate_solutions(col + 1, board, solutions)
    return solutions

def min_moves(input_positions):
    # Time Complexity: O(92 * 8) = O(1) p since we compare input with all 92 valid solutions
    # Space Complexity: O(92*8) = O(1)  storing all 92 solutions.
    solutions = generate_solutions()
    min_moves = float('inf')
    for sol in solutions:
        #count how many columns differ from the current solution
        moves = sum(1 for i in range(8) if sol[i] != input_positions[i])
        min_moves = min(min_moves, moves)
    return min_moves

# ------------------ TEST SUITE ------------------

if __name__ == "__main__":
    print("=== Task 1: String Permutation Inclusion ===")

    task1_tests = [
        ("ab", "eidbaooo", True),    # "ba" exists
        ("ab", "eidboaoo", False),   # no permutation
        ("adc", "dcda", True),       # "cda" exists
        ("hello", "ooolleoooleh", False),
        ("a", "ab", True)
    ]

    for i, (s1, s2, expected) in enumerate(task1_tests, 1):
        result = checkInclusion(s1, s2)
        print(f"Test {i}: s1='{s1}', s2='{s2}' → {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
print("\n=== Task 2: 8 Queens Minimum Moves ===")

# Generate all valid solutions once
valid_solutions = generate_solutions()

task2_tests = [
    ([1, 2, 3, 4, 5, 6, 7, 8], 7),   # clearly invalid
    ([1, 1, 1, 1, 1, 1, 1, 1], 7),   # clearly invalid
    (valid_solutions[0], 0),          # guaranteed valid solution
    (valid_solutions[5], 0),          # another valid solution
    (valid_solutions[10], 0),         # another valid solution
]

for i, (pos, expected) in enumerate(task2_tests, 1):
    result = min_moves(pos)
    print(f"Test {i}: input={pos} → {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
