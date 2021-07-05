class BinaraySearchTree():

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def addNode(self,node):
		if node == self.data :
			return print("Duplicate element...")
		if self.data < node:
			if self.right:
				self.right.addNode(node)
			else:
				self.right = BinaraySearchTree(node)
		else:
			if self.left:
				self.left.addNode(node)
			else:
				self.left = BinaraySearchTree(node)

	def getHeight(self):
		pass

	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print(self.data,end="  ")
			if self.right:
				self.right.inorder()

	def search(self,element):
		if self.data == element:
			return True
		elif self.data < element :
			if self.right:
				return self.right.search(element)
		else:
			if self.left:
				return self.left.search(element)
		return False

	def deleteNode(self,node):
		pass

	def invertTree(self):
		if self:
			if self.left:
				self.left.invertTree()
			if self.right:
				self.right.invertTree()
			self.right, self.left = self.left,self.right

	def minNode(self):
		if self.left:
			return self.left.minNode()
		return self.data

	def maxNode(self):
		if self.right:
			return self.right.maxNode()
		return self.data
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__=="__main__":
	root = BinaraySearchTree(6)
