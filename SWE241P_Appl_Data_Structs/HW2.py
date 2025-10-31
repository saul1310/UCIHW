# Task-1: Given an array of integer nums sorted in non-decreasing order, find a given target value's first and last position. 
# Suppose the target is not found in the array; return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.
# Also, write additional sample test cases to validate your implementation.

#Time complexity: O(log n)
#space complexity: O(1)
def find_first_last(nums, target):
    #both sub functions have a time complexity of O(log n), since they are both just binary searches
    
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid      # save the location of the current most left found 
                right = mid - 1  # keep searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid #save the location of the current most right found
                left = mid + 1  # keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    return [find_first(nums, target), find_last(nums, target)]

test = [1,3,5,5,5,7,8,10]
print (find_first_last(test,5))
# ------------------------------------
# Task 2:
# Search for a target within a 2d matrix
# we treat this matrix like a flattened list of length n * m.
#We then  carry out a normal binary search on this theoretical flattened list, and relate it to the actual structure by 
#using a 1d to 2d mapping formula i = k //n, j = k % n to find its actual position in the matrix.

# k → the index in the flattened 1D array (0-based).

# n → the number of columns in the matrix.

# i → the row index in the 2D matrix.

# j → the column index in the 2D matrix.

# Runtime complexity: O(log(m⋅n))
# Space complexity: O(1)
def searchmatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    #matrix is square, so m * n is length
    m,n = len(matrix),len(matrix[0])
    #left right are assinged to the left and right side of the "list"
    left,right = 0,m*n-1
    while left <= right:
        # find the midpoint of the size of the "list"
        mid = (left+right)//2
        #find the row and column in our matrix that this correlates to
        row = mid // n
        column = mid % n
        #check if that value is our target
        mid_val = matrix[row][column]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid +1
        else:
            right = mid -1
    return False

# ------------------ TEST SUITE ------------------

if __name__ == "__main__":
    print("=== Task 1: Find First and Last Position ===\n")

    task1_tests = [
        ([1, 3, 5, 5, 5, 7, 8, 10], 5, [2, 4]),  # multiple occurrences
        ([1, 2, 3, 4, 5], 3, [2, 2]),           # single occurrence
        ([1, 2, 3, 4, 5], 6, [-1, -1]),         # target not in array
        ([5, 5, 5, 5], 5, [0, 3]),              # all elements same as target
        ([], 1, [-1, -1]),                      # empty array
        ([1], 1, [0, 0]),                        # single element matches
        ([1], 2, [-1, -1]),                      # single element no match
    ]

    for i, (nums, target, expected) in enumerate(task1_tests, 1):
        result = find_first_last(nums, target)
        print(f"Test {i}: nums={nums}, target={target} → {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")

    print("\n=== Task 2: Search in 2D Matrix ===\n")

    task2_tests = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),                          # single element matrix match
        ([[1]], 2, False),                         # single element matrix no match
        ([[]], 1, False),                          # empty matrix
        ([[1,2,3],[4,5,6],[7,8,9]], 9, True),     # last element
        ([[1,2,3],[4,5,6],[7,8,9]], 0, False),    # element less than min
    ]

    for i, (matrix, target, expected) in enumerate(task2_tests, 1):
        result = searchmatrix(matrix, target)
        print(f"Test {i}: target={target} in matrix → {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")
