class Solution(object):
  def searchInsert(self, nums, target):
    lo = 0
    hi = len(nums)
    while lo < hi:
      mid = lo + (hi - lo) / 2
      if nums[mid] > target:
        hi = mid
      elif nums[mid] < target:
        lo = mid + 1
      else:
        return mid
    return lo