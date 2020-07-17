"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

输入: [1,3,5,6], 5
输出: 2

输入: [1,3,5,6], 2
输出: 1

输入: [1,3,5,6], 7
输出: 4

输入: [1,3,5,6], 0
输出: 0
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)

    while right > left:
        pivot = (left + right) // 2
        if nums[pivot] > target:
            right = pivot
        elif nums[pivot] < target:
            left = pivot + 1
        else:
            return pivot

    return left

a = [1, 3, 5, 6]
# a = [1, 3]
# b = 1
b = 7
print(searchInsert(a, b))