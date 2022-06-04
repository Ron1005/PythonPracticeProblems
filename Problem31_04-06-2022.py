#LeetCode Problem : 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

#Example

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# My Solution

# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         itr = head
#         count = 0
#         while itr:
#             itr = itr.next
#             count += 1
#         if count % 2 != 0:
#             mid = (count + 1) / 2
#         else:
#             mid = (count / 2) + 1
#
#         itr2 = head
#         count2 = 1
#         while count2 != mid:
#             itr2 = itr2.next
#             count2 += 1
#
#         return itr2

# Proposed Solution

# slow counter moves one step forward while fast counter moves two step forward.
# When fast counter reaches at the end of the linked list the slow counter is present at the middle
# Hence we return value of slow
# def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow