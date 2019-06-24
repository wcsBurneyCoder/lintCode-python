#coding: utf-8
'''
二分查找
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
'''

def binarySearch(nums, target):
	if not nums:
		return -1

	start = 0
	end = len(nums) - 1
	while start < end:
		mid = start + (end - start) // 2
		if nums[mid] == target:
			end = mid
		elif nums[mid] < target:
			start = mid + 1
		else:
			end = mid - 1

	if nums[start] == target:
		return start

	return -1
    