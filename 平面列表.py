# coding:utf-8
'''
平面列表
给定一个列表，该列表中的每个元素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。
请用非递归方法尝试解答这道题。
样例  1:
	输入: [[1,1],2,[1,1]]
	输出:[1,1,2,1,1] 
	
	样例解释:
	将其变成一个只包含整数的简单列表。


样例 2:
	输入: [1,2,[1,2]]
	输出:[1,2,1,2]
	
	样例解释: 
	将其变成一个只包含整数的简单列表。
	
样例 3:
	输入:[4,[3,[2,[1]]]]
	输出:[4,3,2,1]
	
	样例解释: 
	将其变成一个只包含整数的简单列表。
'''

#非递归
# def flatten(nestedList):
# 	# Write your code here
# 	result = []
# 	while len(nestedList) > 0:
# 		popEliment = nestedList.pop(0)
# 		if isinstance (popEliment,list):
# 			popEliment.extend(nestedList)
# 			nestedList = popEliment
# 		else:
# 			result.append(popEliment)
# 	return result

#递归
def flatten(nestedList):
	# Write your code here
	if isinstance(nestedList, int):
		return [nestedList]
		
	result = []
	for item in nestedList:
		result.extend(flatten(item))
	return result


if __name__ == '__main__':
	num_list = [[1,1],2,[1,1]]
	print(flatten(num_list))