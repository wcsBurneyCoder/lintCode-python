#coding:utf-8
'''
合并排序数组
合并两个有序升序的整数数组A和B变成一个新的数组。新数组也要有序。
输入: A=[1], B=[1]
输出:[1,1]	
样例解释: 返回合并后的数组。

输入: A=[1,2,3,4], B=[2,4,5,6]
输出: [1,2,2,3,4,4,5,6]	
样例解释: 返回合并后的数组。
'''

def mergeSortedArray(A, B):
	# write your code here
	if not len(A): return B
	if not len(B): return A

	mergeArray = A + B
	mergeArray.sort()
	return mergeArray

if __name__ == '__main__':
	list1 = [1,2,3,4]
	list2 = [2,4,5,6]
	print(mergeSortedArray(list1, list2))
