#LeetCode Problem : 1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
#
# Return the decimal value of the number in the linked list.

#Example
# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#My Solution
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         itr = head
#         binstring=""
#         while itr:
#             binstring=binstring + str(itr.val)
#             itr=itr.next
#         return int(binstring,2)




#Proposed Solution

# Think about turning a binary digit into a decimal digit by multiplying by 2, starting from the largest (head) digit.
#
# binary: 1001
# decimal 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0
#
# The pattern here is we add the current digit, then as we move on to the next digit, we multiply all previous digits by 2.
# This way, we get the effect of multiplying each digit of binary by 2 the correct number of times.
# def getDecimalValue(self, head: ListNode) -> int:
#     answer = 0
#     while head:
#         answer = 2* answer + head.val
#         head = head.next
#     return answer