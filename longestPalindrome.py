class Solution:
    def longestPalindrome(self, s: str) -> str:
        sprime = '$' + '$'.join(s) +'$'
        slength = len(sprime)
        palindromeRadiiDict = {}
        print(s)
        center = 0
        radius = 0
        while center < slength:
            while center - (radius + 1) >= 0 and center + (radius + 1) < slength and sprime[center - (radius + 1)] == sprime[center + (radius + 1)]:
                radius += 1
            palindromeRadiiDict[center] = radius
            oldCenter = center
            oldRadius = radius
            center += 1
            radius = 0
            while center <= oldCenter + oldRadius:
                mirroredCenter = oldCenter - (center - oldCenter)
                maxMirroredRadius = oldCenter + oldRadius - center
                if palindromeRadiiDict[mirroredCenter] < maxMirroredRadius:
                    palindromeRadiiDict[center] = palindromeRadiiDict[mirroredCenter]
                    center += 1
                elif palindromeRadiiDict[mirroredCenter] > maxMirroredRadius:
                    palindromeRadiiDict[center] = maxMirroredRadius
                    center += 1
                else:
                    radius = maxMirroredRadius
                    break
        longestPalindromeInSprime = 0
        longestPalindromeCenter = 0
        for k, v in palindromeRadiiDict.items():
            if v > longestPalindromeInSprime:
                longestPalindromeCenter = k
                longestPalindromeInSprime = v
        start = (longestPalindromeCenter - longestPalindromeInSprime) // 2
        end = (longestPalindromeCenter + longestPalindromeInSprime) // 2
        re = s[start: end]
        longestPalindromeInSprime = 2 * max(palindromeRadiiDict.values()) + 1
        longestPalindromeInS = (longestPalindromeInSprime - 1) / 2
        return re

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest = 1
#         longestStr = s[0]
#         slength = len(s)
#         input = list(s)
#         crdict = {}
#         largestr = 0
#         for i in range(slength):
#             pre = i
#             post = i
#             if i not in crdict:
#                 crdict[i] = 0
#             while input[pre] == input[post]:
#                 l = post - pre + 1
#                 if l > longest:
#                     longest = l
#                     longestStr = s[pre:post + 1]
#                     largestr = post - i
#                 r = post - i
#                 if r > crdict[i]:
#                     crdict[i] = r
#                 pre -= 1
#                 post += 1
#                 if pre < 0 or post >= slength:
#                     break
#             # if i not in crdict:
#             #     crdict[i] = post - i
#             if i < slength - 1:
#                 pre = i
#                 post = i + 1
#                 while input[pre] == input[post]:
#                     l = post - pre + 1
#                     if l > longest:
#                         longest = l
#                         longestStr = s[pre:post + 1]
#                         largestr = post - i
#                     r = post - i
#                     if r > crdict[i]:
#                         crdict[i] = r
#                     pre -= 1
#                     post += 1
#                     if pre < 0 or post > slength - 1:
#                         break
#                 # if i not in crdict:
#                 #     crdict[i] = post - i
#                 # else:
#                 #     raise Exception("same center found for: " + str(i))
#             if i + largestr >= slength - 1:
#                 break
#         return longestStr
#
#     def _findPalindrome(self, input, longest, longestStr, post, pre, s, slength):
#         while input[pre] == input[post]:
#             l = post - pre + 1
#             if l > longest:
#                 longest = l
#                 longestStr = s[pre:post + 1]
#             pre -= 1
#             post += 1
#             if pre < 0 or post >= slength:
#                 break
#         return longest, longestStr



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         longest = 1
#         longestStr = s[0]
#         slength = len(s)
#         input = list(s)
#         for i in range(slength):
#             pre = i
#             post = i
#             longest, longestStr = self._findPalindrome(input, longest, longestStr, post, pre, s, slength)
#             if i < slength - 1:
#                 pre = i
#                 post = i + 1
#                 longest, longestStr = self._findPalindrome(input, longest, longestStr, post, pre, s, slength)
#         return longestStr
#
#     def _findPalindrome(self, input, longest, longestStr, post, pre, s, slength):
#         while input[pre] == input[post]:
#             l = post - pre + 1
#             if l > longest:
#                 longest = l
#                 longestStr = s[pre:post + 1]
#             pre -= 1
#             post += 1
#             if pre < 0 or post >= slength:
#                 break
#         return longest, longestStr


if __name__ == '__main__':
    input = 'babad'
    s = Solution()
    output = s.longestPalindrome(input)
    print(output)