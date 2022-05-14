#LeetCode Problem : 26.Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

# Example
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

#My Solution
def removeDuplicates(nums) -> int:
        s1 = sorted(list(set(nums)))
        for x in range(0,len(nums)):
            if x<len(s1):
                nums[x] = s1[x]
        return len(s1),nums

#Proposed Solution
def removeDuplicates2(nums) -> int:
    x = 1
    for i in range(len(nums) - 1):
        if (nums[i] != nums[i + 1]):
            nums[x] = nums[i + 1]
            x += 1
    return x,nums

res,nums = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(res)
print(nums)


