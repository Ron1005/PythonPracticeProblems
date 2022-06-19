#LeetCode Problem : 1268. Search Suggestions System

# You are given an array of strings products and a string searchWord.
#
# Design a system that suggests at most three product names from products after each character of searchWord is typed.
# Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return
# the three lexicographically minimums products.
#
# Return a list of lists of the suggested products after each character of searchWord is typed.

#Example

# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]


#Solution

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         resarray = []
#         newlist = sorted(products)
#         for x in range(1, len(searchWord) + 1):
#             temp = searchWord[0:x]
#             count = 0
#             templist = []
#             for y in newlist:
#                 if len(y) >= x:
#                     temp1 = y[0:x]
#                     if temp == temp1:
#                         templist.append(y)
#                         count += 1
#                         if count == 3:
#                             break
#             resarray.append(templist)
# 
#         return resarray
