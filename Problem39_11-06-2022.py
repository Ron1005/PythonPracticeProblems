#LeetCode Problem : 206. Reverse Linked List

#Given the head of a singly linked list, reverse the list, and return the reversed list.

#Example:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

#Solution



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         def reversify(prevNode, currentNode, nextNode):
#             if currentNode.next == None:
#                 currentNode.next = prevNode
#                 return currentNode
#
#             currentNode.next = prevNode
#
#             return reversify(currentNode, nextNode, nextNode.next)
#
#         if (head):
#             DemoNode = reversify(None, head, head.next)
#             return DemoNode
#         else:
#             return head

