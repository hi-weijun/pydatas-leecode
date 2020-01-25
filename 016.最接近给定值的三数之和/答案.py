class Solution(object):
  def threeSumClosest(self, nums, target):
    """
    :nums类型: List[int]
    :target类型: int
    :返回类型: int
    """
    nums.sort()  #还是先排序
    ans = 0
    diff = float("inf")
    for i in range(0, len(nums)):
      start, end = i + 1, len(nums) - 1
      while start < end:
        sum = nums[i] + nums[start] + nums[end]
        if sum > target:
          if abs(target - sum) < diff:
            diff = abs(target - sum)
            ans = sum
          end -= 1
        else:
          if abs(target - sum) < diff:
            diff = abs(target - sum)
            ans = sum
          start += 1
    return ans