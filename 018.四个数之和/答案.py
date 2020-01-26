class Solution(object):
  def fourSum(self, nums, target):
    """
    :nums类型: List[int]
    :target类型: int
    :返回类型: List[List[int]]
    """
    nums.sort()      #整体思路，先排序再左右夹逼
    res = []
    for i in range(0, len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      for j in range(i + 1, len(nums)):
        if j > i + 1 and nums[j] == nums[j - 1]:
          continue
        start = j + 1
        end = len(nums) - 1
        while start < end:
          sum = nums[i] + nums[j] + nums[start] + nums[end]
          if sum < target:
            start += 1
          elif sum > target:
            end -= 1
          else:
            res.append((nums[i], nums[j], nums[start], nums[end]))
            start += 1
            end -= 1
            while start < end and nums[start] == nums[start - 1]:
              start += 1
            while start < end and nums[end] == nums[end + 1]:
              end -= 1
    return res