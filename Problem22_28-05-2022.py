#LeetCode Problem : 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

#Example
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.

#Note: Formula n*(n+1)/2 is used to find the sum of n natural numbers and then this sum is subtracted from array's sum to
#find the missing number

def missingNumber(nums) -> int:
    sumofnums = sum(nums)
    sum0 = len(nums) * (len(nums) + 1) // 2
    return sum0 - sumofnums

print(missingNumber([0,1,2]))