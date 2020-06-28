"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
"""
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()
    length = len(nums)
    sum_closest = nums[0] + nums[1] + nums[-1]
    min_gap = abs(sum_closest - target)
    for i in range(length):
        index1 = i + 1
        index2 = length - 1
        while index1 < index2:
            nums_sum = nums[i] + nums[index1] + nums[index2]
            gap = nums_sum - target
            if abs(gap) < min_gap:
                min_gap = abs(gap)
                sum_closest = nums_sum
            if nums_sum > target:
                index2 -= 1
            elif nums_sum < target:
                index1 += 1
            else:
                return target

    return sum_closest


a = [-1, 2, 1, -4]
b = 1
print(three_sum_closest(a, b))