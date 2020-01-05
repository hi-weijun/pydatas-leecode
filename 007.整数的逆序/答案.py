class Solution(object):
  def reverse(self, x):
    """
    :x的类型: int
    :返回值类型: int
    """
    sign = x < 0 and -1 or 1
    x = abs(x)
    ans = 0
    while x:
      ans = ans * 10 + x % 10
      x /= 10
    return sign * ans if ans <= 0x7fffffff else 0

#可以算一下 0x7FFFFFFF 是多少
#每个十六进制数4bit，因此8位16进制是4个字节，刚好是一个int整型
#F (十进制的16)的二进制码为 1111
#7的二进制码为 0111
#这样一来，整个整数 0x7FFFFFFF 的二进制表示就是除了首位是 0，其余都是1
#就是说，这是最大的整型数 int（因为第一位是符号位，0 表示它是正数）