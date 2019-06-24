# coding:utf-8
'''
反转一个3位整数
样例 1:
输入: number = 123
输出: 321
样例 2:
输入: number = 900
输出: 9
'''

def reverseInteger(number):
	num_list = list(str(number))
	num_list.reverse()
	return int("".join(num_list))


if __name__ == '__main__':
	print (reverseInteger(123))
	print (reverseInteger(900))