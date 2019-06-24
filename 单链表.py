#coding:utf-8
'''
计算链表中有多少个节点.
样例  1:
	输入:  1->3->5->null
	输出: 3
	
	样例解释: 
	返回链表中结点个数，也就是链表的长度.

样例 2:
	输入:  null
	输出: 0
	
	样例解释: 
	空链表长度为0
'''

class linkNode(object):
	"""docstring for linkNode"""
	def __init__(self, val, next = None):
		super(linkNode, self).__init__()
		self.val = val
		self.next = next


class singleLink(object):
	"""docstring for singleLink"""
	def __init__(self, head = None):
		super(singleLink, self).__init__()
		self.head = head
		self.tail = head

	def addNode(self, node):
		if self.tail:
			self.tail.next = node
			self.tail = node
		else:
			self.head = node
			self.tail = node

	def count(self):
		number = 0
		head = self.head
		while head:
			number += 1
			head = head.next
		return number


if __name__ == '__main__':
	
	link = singleLink()
	link.addNode(linkNode(1))
	link.addNode(linkNode(3))
	link.addNode(linkNode(5))
	print (link.count())

		
