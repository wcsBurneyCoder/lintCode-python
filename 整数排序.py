#coding:utf-8
'''
整数排序
给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。
样例  1:
	输入:  [3, 2, 1, 4, 5]
	输出:  [1, 2, 3, 4, 5]
	
	样例解释: 
	返回排序后的数组。

样例 2:
	输入:  [1, 1, 2, 1, 1]
	输出:  [1, 1, 1, 1, 2]
	
	样例解释: 
	返回排好序的数组。
'''

def sortIntegers(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):
            if A[min] > A[j]:
                min = j
        if i != min:
            A[min],A[i] = A[i],A[min]


if __name__ == '__main__':
	target = [3,2,1,4,5]
	sortIntegers(target)
	print (target)