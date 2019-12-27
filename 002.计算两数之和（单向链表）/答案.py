#首先需要了解python单项链表的底层数据结构
# 定义一个单项链表
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
  # 这个可能是初次想到的标准解决思路
  def _addTwoNumbers(self, l1, l2):
    """
    :l1类型: ListNode
    :l2类型: ListNode
    :返回类型: ListNode
    """
    p = dummy = ListNode(-1)
    carry = 0
    while l1 and l2:
      p.next = ListNode(l1.val + l2.val + carry)
      carry = p.next.val / 10
      p.next.val %= 10  #产生进位
      p = p.next
      l1 = l1.next
      l2 = l2.next

    res = l1 or l2
    while res:
      p.next = ListNode(res.val + carry)
      carry = p.next.val / 10
      p.next.val %= 10
      p = p.next
      res = res.next
    if carry:
      p.next = ListNode(1)
    return dummy.next


  # 更简短（灵性）的解决答案版本
  def addTwoNumbers(self, l1, l2):
    p = dummy = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
      val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
      carry = val / 10
      p.next = ListNode(val % 10)
      l1 = l1 and l1.next
      l2 = l2 and l2.next
      p = p.next
    return dummy.next