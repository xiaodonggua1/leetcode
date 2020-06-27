"""
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
 
提示：

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
"""
from typing import List


# def firstMissingPositive(nums: List[int]) -> int:
#     min_num = 0
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i] > min_num:
#             gap = nums[i] - min_num
#             if gap == 1:
#                 min_num = nums[i]
#             else:
#                 return min_num + 1
#     return min_num + 1

def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(len(nums)):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

    for i in range(n):
        if nums[i] != i +1:
            return i + 1

    return n + 1

a = [7,8,9,11,12]
print(firstMissingPositive(a))