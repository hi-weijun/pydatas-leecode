最先开始想到的
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n == 0 or n == 1 else self.climbStairs(n - 1) + self.climbStairs(n - 2)
# 超时了，意料之中


#然后DP

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        climb = dict()
        climb[0], climb[1] = 1, 1
        for i in range(2, n + 1):
            climb[i] = climb[i - 1] + climb[i- 2]
        return climb[n]


#实际上这个问题是斐波那契数列的变形

class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 1:
      return 1
    pre, ppre = 1, 1
    for i in range(2, n + 1):
      tmp = pre
      pre = ppre + pre
      ppre = tmp
    return pre