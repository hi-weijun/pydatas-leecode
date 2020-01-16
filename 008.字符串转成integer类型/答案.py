class Solution(object):
  def myAtoi(self, s):
    """
    :需转换的类型 str: str
    :返回类型: int
    """
    s = s.strip()
    sign = 1
    if not s:
      return 0
    if s[0] in ["+", "-"]:
      if s[0] == "-":
        sign = -1
      s = s[1:]
    ans = 0
    for c in s:
      if c.isdigit():
        ans = ans * 10 + int(c)
      else:
        break
    ans *= sign
    if ans > 2147483647:   #正确的值超出可表示值的范围
      return 2147483647
    if ans < -2147483648:
      return -2147483648
    return ans