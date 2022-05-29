#LeetCode Problem : 318. Maximum Product of Word Lengths

# Given a string array words, return the maximum value of length(word[i]) * length(word[j])
# where the two words do not share common letters.
# If no such two words exist, return 0.


#Example
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

#My Solution
def maxProduct(words) -> int:
    d1 = {x: len(x) for x in words}
    maximum = 0
    for word in d1.keys():
        for word2 in d1.keys():
            if word != word2:
                commonletter = False
                for letter in word:
                    if letter in word2:
                        commonletter = True
                        break
                if not commonletter:
                    product = d1[word] * d1[word2]
                    if product > maximum:
                        maximum = product

    return maximum

print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))

#Proposed Solution

#Proposed Soluion uses bit manipulation technique which we will learn in future.