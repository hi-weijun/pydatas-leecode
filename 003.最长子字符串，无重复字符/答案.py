import collections
class Solution(object):
  def _lengthOfLongestSubstring(self, s):
    """
    :数据s类型: str
    :返回类型: int
    """
    d = collections.defaultdict(int)
    #该函数返回一个类似字典的对象。
    # defaultdict是Python内建字典类（dict）的一个子类，它重写了方法_missing_(key)，
    # 增加了一个可写的实例变量default_factory,实例变量default_factory被missing()方法使用，如果该变量存在，
    # 则用以初始化构造器，如果没有，则为None。其它的功能和dict一样。
    l = ans = 0
    for i, c in enumerate(s):
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
        # 一般用在 for 循环当中。
      while l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = max(ans, l)
    return ans

  def lengthOfLongestSubstring(self, s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
      if c in d:
        start = max(start, d[c] + 1)
      d[c] = i
      ans = max(ans, i - start + 1)
    return ans