class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
# class Solution(object):
#     def findMedian(self, l):
#         length = len(l)
#         if length == 0:
#             return
#         if length % 2 == 1:
#             return l[length // 2]
#         if length % 2 == 0:
#             return (l[length // 2 - 1] + l[length // 2]) / 2
#
#     def findMedian2(self, l, n):
#         length = len(l)
#         if length == 0:
#             return n
#         if length == 1:
#             return (n + l[0]) / 2
#         if length == 2:
#             if n < l[0]:
#                 return l[0]
#             elif n > l[1]:
#                 return l[1]
#             else:
#                 return n
#         if length % 2 == 1:
#             m = l[length // 2]
#             if n < m:
#                 mminus1 = l[length // 2 - 1]
#                 if n < mminus1:
#                     return (mminus1 + m) / 2
#                 else:
#                     return (n + m) / 2
#             else:
#                 mplus1 = l[length // 2 + 1]
#                 if n < mplus1:
#                     return (n + m) / 2
#                 else:
#                     return (mplus1 + m) / 2
#         if length % 2 == 0:
#             mminus1 = l[length // 2 - 1]
#             mplus1 = l[length // 2]
#             if n <= mminus1:
#                 return mminus1
#             elif n >= mplus1:
#                 return mplus1
#             else:
#                 return n
#
#     def findMedian3(self, l, n1, n2):
#         length = len(l)
#         if length == 0:
#             return (n1 + n2) / 2
#         if length == 1:
#             if l[0] < n1:
#                 return n1
#             elif l[0] > n2:
#                 return n2
#             else:
#                 return l[0]
#         if length == 2:
#             if l[0] >= n2:
#                 return (n2 + l[0]) / 2
#             if l[1] <= n1:
#                 return (n1 + l[1]) / 2
#             if l[0] <= n1 < l[1] <= n2:
#                 return (n1 + l[1]) / 2
#             if l[0] <= n1 and n2 < l[1]:
#                 return (n1 + n2) / 2
#             if n1 < l[0] and l[1] <= n2:
#                 return (l[0] + l[1]) / 2
#             if n1 < l[0] < n2 < l[1]:
#                 return (l[0] + n2) / 2
#         if length % 2 == 1:
#             m = l[length // 2]
#             if m < n1:
#                 mplus1 = l[length // 2 + 1]
#                 if mplus1 < n1:
#                     return mplus1
#                 else:
#                     return n1
#             elif m > n2:
#                 mminus1 = l[length // 2 - 1]
#                 if mminus1 > n2:
#                     return mminus1
#                 else:
#                     return n2
#             else:
#                 return m
#         if length % 2 == 0:
#             mminus2 = l[length // 2 - 2]
#             mminus1 = l[length // 2 - 1]
#             mplus1 = l[length // 2]
#             mplus2 = l[length // 2 + 1]
#             if n2 <= mminus2:
#                 return (mminus2 + mminus1) / 2
#             if mminus2 < n2 <= mminus1:
#                 return (n2 + mminus1) / 2
#             if mminus1 < n2 <= mplus1:
#                 if n1 <= mminus1:
#                     return (n2 + mminus1) / 2
#                 else:
#                     return (n1 + n2) / 2
#             if mplus1 <= n2 <= mplus2:
#                 if n1 > mminus1:
#                     return (n1 + mplus1) / 2
#                 else:
#                     return (mminus1 + mplus1) / 2
#             # if mminus1 < n1 and mplus1 < n2:
#             #     return (n1 + mplus1) / 2
#             # if mplus2 > n1 >= mplus1:
#             #     return (n1 + mplus1) / 2
#             if n2 >= mplus2:
#                 if n1 <= mminus1:
#                     return (mminus1 + mplus1) / 2
#                 elif n1 >= mplus2:
#                     return (mplus2 + mplus1) / 2
#                 else:
#                     return (n1 + mplus1) / 2
#
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         l1 = len(nums1)
#         l2 = len(nums2)
#         if l1 == 0:
#             return self.findMedian(nums2)
#         if l2 == 0:
#             return self.findMedian(nums1)
#         if l1 == 1:
#             return self.findMedian2(nums2, nums1[0])
#         if l2 == 1:
#             return self.findMedian2(nums1, nums2[0])
#         if l1 == 2:
#             return self.findMedian3(nums2, nums1[0], nums1[1])
#         if l2 == 2:
#             return self.findMedian3(nums1, nums2[0], nums2[1])
#         if l1 % 2 == 0:
#             m1index = l1 // 2 - 1
#             m1 = (nums1[m1index] + nums1[m1index + 1]) / 2
#         else:
#             m1index = l1 // 2
#             m1 = nums1[m1index]
#         if l2 % 2 == 0:
#             m2index = l2 // 2 - 1
#             m2 = (nums2[m2index] + nums2[m2index + 1]) / 2
#         else:
#             m2index = l2 // 2
#             m2 = nums2[m2index]
#         # m1 = l1 // 2
#         # m2 = l2 // 2
#         i = min(m1index, m2index)
#         if m1 >= m2:
#             return self.findMedianSortedArrays(nums1[0:l1 - i], nums2[i:])
#             # m = l2 // 2
#             # nums1[m2]
#         else:
#             return self.findMedianSortedArrays(nums1[i:], nums2[0:l2 - i])


if __name__ == '__main__':
    # l1 = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17,18,19,20,22,23,24,25,27,36]
    # l2 = [103,104,105,108,200,201,202,211,212,213,213,214,222,223,225]
    l1 = [1]
    l2 = [1,2]
    s = Solution()
    re = s.findMedianSortedArrays(l1, l2)
    print(re)
