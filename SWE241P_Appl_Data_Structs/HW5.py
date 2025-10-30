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