# coding:utf-8
'''
Fizz Buzz 问题
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
如果这个数既不能被 3 整除也不能被 5 整除，打印数字本身。
只用一个 if 来实现

样例
比如 n = 15, 返回一个字符串数组：

[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
'''

def fizzBuzz(n):
	# write your code here
	rst = []
	for i in range(1, n + 1):
		rst.append(str(i))
	for i in range(2, n, 3):
		rst[i] = "fizz"
	for i in range(4, n, 5):
		if rst[i] == "fizz":
			rst[i] = "fizz buzz"
			continue
		rst[i] = "buzz"
	return rst


if __name__ == '__main__':
	print(fizzBuzz(15))