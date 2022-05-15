#LeetCode Problem : 13. Roman to Integer
#Convert Roman String to Integer
#My Solution

def romanToInt(s: str) -> int:
        # rtonmapping={}
        # rtonmapping["I"] = 1
        # rtonmapping["V"] = 5
        # rtonmapping["X"] = 10
        # rtonmapping["L"] = 50
        # rtonmapping["C"] = 100
        # rtonmapping["D"] = 500
        # rtonmapping["M"] = 1000
        res = 0
        skip = False
        for x in range(0, len(s)):
            y = x + 1
            if (skip):
                skip = False
                continue
            if s[x] == "I":
                if y < len(s) and s[y] == "V":
                    res = res + 4
                    skip = True
                elif y < len(s) and s[y] == "X":
                    res = res + 9
                    skip = True
                else:
                    res = res + 1
            elif s[x] == "V":
                res = res + 5
            elif s[x] == "X":
                if y < len(s) and s[y] == "L":
                    res = res + 40
                    skip = True
                elif y < len(s) and s[y] == "C":
                    res = res + 90
                    skip = True
                else:
                    res = res + 10
            elif s[x] == "L":
                res = res + 50
            elif s[x] == "C":
                if y < len(s) and s[y] == "D":
                    res = res + 400
                    skip = True
                elif y < len(s) and s[y] == "M":
                    res = res + 900
                    skip = True
                else:
                    res = res + 100
            elif s[x] == "D":
                res = res + 500
            elif s[x] == "M":
                res = res + 1000
        return res

#Proposed Solution
# def romanToInt(self, s: str) -> int:
# 	res, prev = 0, 0
# 	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# 	for i in s[::-1]:          # rev the s
# 		if dict[i] >= prev:
# 			res += dict[i]     # sum the value if previous value same or more
# 		else:
# 			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
# 		prev = dict[i]
# 	return res


response = romanToInt("III")
print(response)
