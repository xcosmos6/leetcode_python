# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addition(l1, l2, 0)

    def addition(self, l1, l2, r):
        result = ListNode()
        if l1 != None and l2 != None:
            a = l1.val + l2.val + r
            r = 0
            if a >= 10:
                a = a - 10
                r = 1
            result.val = a
            result.next = self.addition(l1.next, l2.next, r)
            return result
        elif l1 == None and l2 != None:
            a = l2.val + r
            r = 0
            if a >= 10:
                a = a - 10
                r = 1
            result.val = a
            result.next = self.addition(None, l2.next, r)
            return result
        elif l1 != None and l2 == None:
            a = l1.val + r
            r = 0
            if a >= 10:
                a = a - 10
                r = 1
            result.val = a
            result.next = self.addition(l1.next, None, r)
            return result
        else:
            if r != 0:
                result.val = r
                result.next = None
                return result
            else:
                return None

# if __name__ == '__main__':
#     list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
#     list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
#     s = Solution()
#     r = s.addTwoNumbers(list1, list2, 0)
#     print(r.val, r.next.val, r.next.next.val)


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2, r):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         result = ListNode()
#         if l1 != None and l2 != None:
#             a = l1.val + l2.val + r
#             r = 0
#             if a >= 10:
#                 a = a - 10
#                 r = 1
#             result.val = a
#             result.next = self.addTwoNumbers(l1.next, l2.next, r)
#             return result
#         elif l1 == None and l2 != None:
#             a = l2.val + r
#             r = 0
#             if a >= 10:
#                 a = a - 10
#                 r = 1
#             result.val = a
#             result.next = self.addTwoNumbers(None, l2.next, r)
#             return result
#         elif l1 != None and l2 == None:
#             a = l1.val + r
#             r = 0
#             if a >= 10:
#                 a = a - 10
#                 r = 1
#             result.val = a
#             result.next = self.addTwoNumbers(l1.next, None, r)
#             return result
#         else:
#             if r != 0:
#                 result.val = r
#                 result.next = None
#                 return result
#             else:
#                 return None
#
# if __name__ == '__main__':
#     list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
#     list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
#     s = Solution()
#     r = s.addTwoNumbers(list1, list2, 0)
#     print(r.val, r.next.val, r.next.next.val)

# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# # class Solution(object):
# def addTwoNumbers(l1, l2, r=0):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#     result = ListNode()
#     if l1 != None and l2 != None:
#         a = l1.val + l2.val + r
#         r = 0
#         if a >= 10:
#             a = a - 10
#             r = 1
#         result.val = a
#         result.next = addTwoNumbers(l1.next, l2.next, r)
#         return result
#     elif l1 == None and l2 != None:
#         a = l2.val + r
#         r = 0
#         if a >= 10:
#             a = a - 10
#             r = 1
#         result.val = a
#         result.next = addTwoNumbers(None, l2.next, r)
#         return result
#     elif l1 != None and l2 == None:
#         a = l1.val + r
#         r = 0
#         if a >= 10:
#             a = a - 10
#             r = 1
#         result.val = a
#         result.next = addTwoNumbers(l1.next, None, r)
#         return result
#     else:
#         if r != 0:
#             result.val = r
#             result.next = None
#             return result
#         else:
#             return None
#
# if __name__ == '__main__':
#     list1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
#     list2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
#     r = addTwoNumbers(list1, list2, r=0)
#     print(r.val, r.next.val, r.next.next.val)