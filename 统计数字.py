#coding:utf-8
'''
统计数字
计算数字 k 在 0 到 n 中的出现的次数，k 可能是 0~9 的一个值。

输入：
k = 1, n = 1
输出：
1
解释：
在 [0, 1] 中，我们发现 1 出现了 1 次 (1)。

输入：
k = 1, n = 12
输出：
5
解释：
在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 中，我们发现 1 出现了 5 次 (1, 10, 11, 12)(注意11中有两个1)。
'''

def digitCounts(k, n):
    string = "".join([str(x) for x in range(0, n + 1)])
    num = len(string) - len(string.replace(str(k),"")) // len(str(k))
    return num


if __name__ == '__main__':
	print (digitCounts(1, 1))
	print (digitCounts(1, 12))
