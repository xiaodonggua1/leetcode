"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""
from typing import List


# def minSubArrayLen(s: int, nums: List[int]) -> int:
#     min_len = 0
#     n = len(nums)
#     for i in range(n):
#         num_sum = nums[i]
#         j = i + 1
#         if num_sum >= s:
#             return 1
#         while j < n:
#             num_sum += nums[j]
#             if num_sum >= s:
#                 length = j - i + 1
#                 if min_len == 0:
#                     min_len = length
#                 else:
#                     min_len = min(length, min_len)
#                 break
#             j += 1
#
#     return min_len


def minSubArrayLen(s: int, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    min_len = n + 1
    start, end = 0, 0
    total = 0
    while end < n:
        total += nums[end]
        while total >= s:
            min_len = min(min_len, end - start + 1)
            total -= nums[start]
            start += 1
        end += 1

    return 0 if min_len == n + 1 else min_len


a = 4
b = [1, 4, 4]

print(minSubArrayLen(a, b))