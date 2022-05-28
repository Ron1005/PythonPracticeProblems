#LeetCode Problem : 1342. Number of Steps to Reduce a Number to Zero

# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

#Example

# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

#My Solution

def numberOfSteps(num: int) -> int:
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
            steps += 1
        else:
            num = num - 1
            steps += 1
    return steps

print(numberOfSteps(14))

#Proposed Solution

#Number of steps = number of divisions by 2 + number of subtractions = number of bitshifts + number of subtractions.
# Every non-zero binary number has a leading bit. The algorithm only stops when the leading bit is bitshifted enough to
# become the last bit and then it's subtracted by 1. Thus, number of bitshifts = number of bits that are not the
# leading bit = length of bitstring - 1.
# (Ex. 22 = 10110 requires 4 bitshifts for the number to become 1. 4 = length of bitstring - 1 = 5 - 1).
#
# As the number is shifted, each 1 eventually reaches the least significant bit position (the last, rightmost bit).
# A 1 in the last bit means the number is odd (which causes a subtraction), so the number of subtractions = number of 1s.
#
# number of steps = number of bitshifts + number of subtractions = (length of bitstring - 1) + number of 1s.

# def numberOfSteps(self, num: int) -> int:
#     bitstring = bin(num)[2:]  # [2:] will remove the '0b' that is prepended to each bitstring by bin()
#     return len(bitstring) - 1 + bitstring.count('1')