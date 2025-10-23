def find_first_last(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
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