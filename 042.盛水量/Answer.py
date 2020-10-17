

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        leftmosthigh = [0 for i in range(len(A))]
        leftmax = 0
        for i in range(len(A)):
            if A[i] > leftmax: leftmax = A[i]
            leftmosthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in reversed(range(len(A))):
            if A[i] > rightmax: rightmax = A[i]
            if min(rightmax, leftmosthigh[i]) > A[i]:
                sum += min(rightmax, leftmosthigh[i]) - A[i]
        return sum


class Solution(object):
  def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    ans = left = 0
    right = len(height) - 1
    leftWall = rightWall = float("-inf")
    while left <= right:
      if leftWall <= rightWall:
        ans += max(0, leftWall - height[left])
        leftWall = max(leftWall, height[left])
        left += 1
      else:
        ans += max(0, rightWall - height[right])
        rightWall = max(rightWall, height[right])
        right -= 1
    return ans


