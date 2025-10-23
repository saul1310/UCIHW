def find_first_last(nums, target):
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
                last = mid
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

def searchmatrix(matrix,target):
    if not matrix or not matrix[0]:
        return False
    m,n = len(matrix),len(matrix[0])
    left,right = 0,m*n-1
    while left <= right:
        mid = (left+right)//2
        row = mid // n
        column = mid % n
        mid_val = matrix[row][column]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid +1
        else:
            right = mid -1
    return False

testlist =  [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchmatrix(testlist,3))