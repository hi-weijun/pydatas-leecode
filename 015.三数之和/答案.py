class Solution(object):
  def threeSum(self, nums):
    """
    :nums类型: List[int]
    :返回类型: List[List[int]]
    """
    # 先排序然后双指针
    res = []
    nums.sort()
    for i in range(0, len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      target = 0 - nums[i]
      start, end = i + 1, len(nums) - 1
      while start < end:
        if nums[start] + nums[end] > target:
          end -= 1
        elif nums[start] + nums[end] < target:
          start += 1
        else:
          res.append((nums[i], nums[start], nums[end]))
          end -= 1
          start += 1
          while start < end and nums[end] == nums[end + 1]:
            end -= 1
          while start < end and nums[start] == nums[start - 1]:
            start += 1
    return res