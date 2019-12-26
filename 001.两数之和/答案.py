class Solution(object):
  def twoSum(self, nums, target):
    """
    :nums类型: List[int]
    :目标类型: int
    :返回类型: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i
    # 没有特殊情况处理,因为它假定只有一个解决方案