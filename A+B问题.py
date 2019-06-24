#coding:utf-8
'''
A + B 问题
给出两个整数 a 和 b, 求他们的和，不使用+号
'''

def aplusb(a, b):
    # write your code here
    INT_RANGE = 0xFFFFFFFF
    while b != 0:
        a, b = a ^ b, (a & b) << 1
        a &= INT_RANGE
    return a if a >> 31 <= 0 else a ^ ~INT_RANGE

if __name__ == '__main__':
	print (aplusb(5, 6))
	print (aplusb(100, -100))
	print (aplusb(200000, 3000000))

