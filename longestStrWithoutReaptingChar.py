def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    clist = []
    longest = 0
    charDict = {}
    start = 0
    for c in range(len(s)):
        n = s[c]
        if n in charDict:
            start = max(charDict[n] + 1, start)
            # clist.append(n)
        # else:
        clength = c - start + 1
        if clength > longest:
            longest = clength
            # clength = len(clist)
            # if clength > longest:
            #     longest = clength
            # clist = list(s[start:c + 1])
        charDict[n] = c
    # clength = len(clist)
    # if clength > longest:
    #     longest = clength
    return longest


if __name__ == '__main__':
    s = 'tmmzuxt'
    length = lengthOfLongestSubstring(s)
    print(length)

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         clist = []
#         longest = 0
#         charDict = {}
#         for c in range(len(s)):
#             n = s[c]
#             # if n not in charDict:
#             #     charDict[n] = c
#             # else:
#             #     charDict[n] = c
#             if n not in clist:
#                 clist.append(n)
#             else:
#                 clength = len(clist)
#                 if clength > longest:
#                     longest = clength
#                 start = charDict[n] + 1
#                 clist = list(s[start:c + 1])
#             charDict[n] = c
#         clength = len(clist)
#         if clength > longest:
#             longest = clength
#         return longest