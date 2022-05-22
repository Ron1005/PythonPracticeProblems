#LeetCode Problem: 35. Search Insert Position

# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

#Example:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4

#My Solution:
def searchInsert(nums, target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if (nums[mid] == target):
            return mid
        elif (target > nums[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return start

#Proposed Solution:
#Same as My Solution

l1 = [1,2,5,6,8]
pos = searchInsert(l1,7)
print(pos)