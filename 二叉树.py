#coding:utf-8
'''
二叉树的最大节点
在二叉树中寻找值最大的节点并返回。
输入:
{1,-5,3,1,2,-4,-5}
输出: 3
说明:
这棵树如下所示：
     1
   /   \
 -5     3
 / \   /  \
1   2 -4  -5
'''

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		super(TreeNode, self).__init__()
		self.val = val
		self.left, self.right = None,None

class Tree(object):
	"""docstring for Tree"""
	def __init__(self, tree_list = None):
		super(Tree, self).__init__()
		self.root = None
		self.node_list = []

		if tree_list:
			for x in tree_list:
				self.addNode(x)


	def addNode(self, val):
		node = TreeNode(val)
		if not self.root:
			self.root = node
			self.node_list.append(self.root)
		else:
			avaible_node = self.node_list[0]
			if not avaible_node.left:
				avaible_node.left = node
				self.node_list.append(avaible_node.left)
			elif not avaible_node.right:
				avaible_node.right = node
				self.node_list.pop(0)
	

	def maxNode(self):
		tempNode = self.maxResultNode(self.root)
		return tempNode.val

	def maxResultNode(self, node):
		if not node:
			return node
		l, r = self.maxResultNode(node.left), self.maxResultNode(node.right)
		node = l if l and l.val > node.val else node
		node = r if r and r.val > node.val else node
		return node


if __name__ == '__main__':
	tree_list = [1,-5,3,1,2,-4,-5]
	tree = Tree(tree_list)
	print(tree.maxNode())