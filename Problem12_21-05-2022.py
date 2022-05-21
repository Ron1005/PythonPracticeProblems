#LeetCode Problem : 27.Remove Element

#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The relative order of the elements may be changed.

#Example
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
#### Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#My Solution:
def removeElement(nums, val: int) -> int:
    if len(nums) > 0:
        maxnumber = max(nums)
        maxnumber = maxnumber + 1
        # print(maxnumber)
        count = 0
        for x, y in enumerate(nums):
            if y == val:
                nums[x] = maxnumber
                count += 1
        nums.sort()
        return len(nums) - count
    else:
        return 0

#Proposed Solution
# def removeElement1(nums, val):
#     start, end = 0, len(nums) - 1
#     while start <= end:
#         if nums[start] == val:
#             nums[start], nums[end], end = nums[end], nums[start], end - 1
#         else:
#             start +=1
#     return start

nums = [1,4,5,3,7,2,1]
res = removeElement(nums,1)
print(nums)
