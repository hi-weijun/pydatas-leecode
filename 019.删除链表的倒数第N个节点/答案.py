# 定义一个单链表过程.

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
  def removeNthFromEnd(self, head, n):
    """
    :"头指针"类型: ListNode
    :n的类型: int
    :返回类型: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    fast = slow = dummy

    while n and fast:
      fast = fast.next
      n -= 1

    while fast.next and slow.next:
      fast = fast.next
      slow = slow.next

    slow.next = slow.next.next
    return dummy.next