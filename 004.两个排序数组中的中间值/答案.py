# 二分操作效率较高
class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    # 可以参考一下Python sorted() 函数的底层实现
    m, n = len(a), len(b)
    after = (m + n - 1) / 2
    lo, hi = 0, m
    while lo < hi:
      i = (lo + hi) / 2
      if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
        hi = i
      else:
        lo = i + 1
    i = lo
    nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
    return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2.0

  # sorted() 函数对所有可迭代的对象进行排序操作。
  # sort 与 sorted 区别：
  # sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
  # list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。