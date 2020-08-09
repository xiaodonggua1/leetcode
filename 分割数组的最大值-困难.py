"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
"""
from typing import List


def splitArray(nums: List[int], m: int) -> int:
    def check(x, m, nums):
        list_num, num_sum = 0, 0
        for i in nums:
            if num_sum + i > x:
                list_num += 1
                num_sum = i
            else:
                num_sum += i

        return list_num <= m

    left, right = 0, len(nums)
    pass