# 1.递归解：
class Solution:
    def generateParenthesis(self, n):
        """
        :n的类型: int
        :返回类型: List[str]
        """
        resList = []
        def generate(left,right,res,n):
            if right == n:
                resList.append(res)
            else:
                if left < n:
                    generate(left+1,right,res+'(',n)
                if right < n and right < left:
                    generate(left,right+1,res+')',n)

        generate(0,0,'',n)

        return resList






# 2.解题思路：列举出所有合法的括号匹配，使用深度优先搜索。如果左括号的数量大于右括号的数量的话，就不能产生合法的括号匹配。

class Solution(object):
  def generateParenthesis(self, n):
    """
    :n的类型: int
    :返回类型: List[str]
    """

    def dfs(left, path, res, n):
      if len(path) == 2 * n:
        if left == 0:
          res.append("".join(path))
        return

      if left < n:
        path.append("(")
        dfs(left + 1, path, res, n)
        path.pop()
      if left > 0:
        path.append(")")
        dfs(left - 1, path, res, n)
        path.pop()

    res = []
    dfs(0, [], res, n)
    return res