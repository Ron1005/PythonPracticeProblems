#LeetCode Problem 58. Length of Last Word
# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

#Example
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

#My Solution
def lengthOfLastWord(s: str) -> int:
    l1 = s.split()
    return len(l1[-1])

#Alternate Solution
# def lengthOfLastWord1(s: str) -> int:
#    tail = len(s)-1
#    count=0
#    while tail>=0 and s[tail]==" ":
#        tail=tail-1
#    while tail>=0 and s[tail]!=" ":
#        tail=tail-1
#        count+=1
#    return count

s="This is a Sting"
res = lengthOfLastWord(s)
print(res)




