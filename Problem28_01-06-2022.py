#LeetCode Problem: 35. Search Insert Position

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

#Example
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


#My Solution
def runningSum(nums):
    sum0 = 0
    l1 = []
    for x in nums:
        sum0 = sum0 + x
        l1.append(sum0)

    return l1


print(runningSum([1,2,3,4,5]))

#Proposed Solution Running Sum
# def runningSum(self, nums):
#     for x in range(1, len(nums)):
#         nums[x] = nums[x] + nums[x - 1]
#
#     return nums