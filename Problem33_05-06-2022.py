#LeetCode Problem : 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

#Example
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Recursion Solution
# def reverseString(self, s: List[str]) -> None:
#     """
#     Do not return anything, modify s in-place instead.
#     """
#
#     def swap(s, p1, p2):
#         if p1 >= p2:
#             return s
#         else:
#             s[p1], s[p2] = s[p2], s[p1]
#             p1 += 1
#             p2 -= 1
#             swap(s, p1, p2)
#
#     return swap(s, 0, len(s) - 1)


# Normal Solution
# def reverseString(self, s: List[str]) -> None:
#     """
#     Do not return anything, modify s in-place instead.
#     """
#     if len(s) % 2 == 0:
#         mid = (len(s) / 2) - 1
#     else:
#         mid = len(s) // 2
#
#     p1 = 0
#     p2 = len(s) - 1
#     while p1 <= mid:
#         temp = s[p1]
#         s[p1] = s[p2]
#         s[p2] = temp
#         p1 += 1
#         p2 -= 1
#
#     return s