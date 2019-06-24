#coding:utf-8
'''
交换数组两个元素
给你一个数组和两个索引，交换下标为这两个索引的数字

输入:  [1, 2, 3, 4], index1 = 2, index2 = 3
输出:  交换后你的数组应该是[1, 2, 4, 3]， 不需要返回任何值，只要就地对数组进行交换即可。
样例解释: 就地交换，不需要返回值。
'''

def swapIntegers(A, index1, index2):
    # write your code here
    A[index1],A[index2] = A[index2], A[index1]


if __name__ == '__main__':
	target_list = [1,2,3,4]
	swapIntegers(target_list, 2, 3)
	print(target_list)