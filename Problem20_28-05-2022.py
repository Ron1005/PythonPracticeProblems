#LeetCode Problem : 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices,
# return an empty list. The returned list must be sorted in increasing order.

# Example:
#
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.


#Solution

def targetIndices(nums ,target: int):
    nums.sort()
    res = []
    for x in range(0, len(nums)):
        if nums[x] == target:
            res.append(x)
        if nums[x] > target:
            break
    return res

getres = targetIndices([1,2,20,8,8,9],2)
print(getres)