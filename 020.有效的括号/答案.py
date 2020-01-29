#python实现，直接利用栈
1.
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for si in s:
            if si == '(':
                stack.append(')')
            elif si == '[':
                stack.append(']')
            elif si == '{':
                stack.append('}')
            elif len(stack) == 0 or si != stack.pop():
                return False
        return len(stack) == 0



# 2.利用词典
class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    d = ["()", "[]", "{}"]
    for i in range(0, len(s)):
      stack.append(s[i])
      if len(stack) >= 2 and stack[-2] + stack[-1] in d:
        stack.pop()
        stack.pop()
    return len(stack) == 0