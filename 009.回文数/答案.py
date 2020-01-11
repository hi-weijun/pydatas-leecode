
class Solution(object):

  # 比较平常的算法
  def _isPalindrome(self, x):
    """
    :x类型: int
    :返回类型: bool
    """
    z = x
    y = 0
    while x > 0:
      y = y * 10 + x % 10
      x /= 10
    return z == y



  # 更快的算法
  def isPalindrome(self, x):
    """
    :x类型: int
    :返回类型: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
      return False
    half = 0
    while x > half:
      half = half * 10 + x % 10
      x /= 10
    return x == half or half / 10 == x