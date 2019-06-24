#coding: utf-8
'''
二分查找
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
样例  1:
	输入:[1,4,4,5,7,7,8,9,9,10]，1
	输出: 0
	
	样例解释: 
	第一次出现在第0个位置。

样例 2:
	输入: [1, 2, 3, 3, 4, 5, 10]，3
	输出: 2
	
	样例解释: 
	第一次出现在第2个位置
	
样例 3:
	输入: [1, 2, 3, 3, 4, 5, 10]，6
	输出: -1
	
	样例解释: 
	没有出现过6， 返回-1
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


if __name__ == '__main__':
	num_list = [1,4,4,5,7,7,8,9,9,10]
	print(binarySearch(num_list, 1))
    