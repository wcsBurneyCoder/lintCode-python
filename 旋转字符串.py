# coding:utf-8
'''
旋转字符串
给定一个字符串（以字符数组的形式给出）和一个偏移量，根据偏移量原地旋转字符串(从左向右旋转)
样例 1:

输入:  str="abcdefg", offset = 3
输出:  str = "efgabcd"	
样例解释:  注意是原地旋转，即str旋转后为"efgabcd"
样例 2:

输入: str="abcdefg", offset = 0
输出: str = "abcdefg"	
样例解释: 注意是原地旋转，即str旋转后为"abcdefg"
样例 3:

输入: str="abcdefg", offset = 1
输出: str = "gabcdef"	
样例解释: 注意是原地旋转，即str旋转后为"gabcdef"
样例 4:

输入: str="abcdefg", offset =2
输出: str = "fgabcde"	
样例解释: 注意是原地旋转，即str旋转后为"fgabcde"
样例 5:

输入: str="abcdefg", offset = 10
输出: str = "efgabcd"	
样例解释: 注意是原地旋转，即str旋转后为"efgabcd"
'''

def rotateString(s, offset):
	if len(s) > 0:
		offset = offset % len(s)
	temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
	for i in range(len(temp)):
		s[i] = temp[i]


if __name__ == '__main__':
	string = "abcdefg"
	s_list = list(string)
	rotateString(s_list, 3)
	print(s_list)