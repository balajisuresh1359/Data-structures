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
		if not self:
			return 0
		maxl=maxr=0
		if self.left:
			maxl = self.left.getHeight()
		if self.right:
			maxr = self.right.getHeight()
		maxlr=max(maxr,maxl)+1
		return maxlr

	def inorder(self):
		if self:
			if self.left:
				self.left.inorder()
			print(self.data,end="  ")
			if self.right:
				self.right.inorder()

	def search(self,element):
		if self.data == element:
			return self
		elif self.data < element :
			if self.right:
				return self.right.search(element)
		else:
			if self.left:
				return self.left.search(element)
		return False

	def deleteNode(self,node):
		if self == None:
			return None
		else:
			if self.data > node:
				self.left = self.left.deleteNode(node)
			else:
				if self.data < node:
					self.right = self.right.deleteNode(node)
				else:
					if self.left and self.right:
						t = self.minNode(self.right)
						self.data = t.data
						self.right = self.right.deleteNode(t.data)
					else:
						if self.left == None:
							self = self.right
						else:
							if self.right == None:
								self = self.left
			return self
						
	def getParent(self,data,acc):
		if self.data == data:
			return True
		l=r=False
		if self.data > data:
			if self.left:
				l = self.left.getParent(data,acc)
		else:
			if self.right:
				r = self.right.getParent(data,acc)
		if l or r :
			acc[0] = self
			return False
		return False


	def invertTree(self):
		if self:
			if self.left:
				self.left.invertTree()
			if self.right:
				self.right.invertTree()
			self.right, self.left = self.left,self.right

	def minNode(self,root):
		if root.left:
			return self.minNode(root.left)
		return root

	def maxNode(self):
		if self.right:
			return self.right.maxNode()
		return self.data



	def getGrandParent(self,data,acc):
		self.getParent(data,acc)
		self.getParent(acc[0],acc)

	def getParentList(self,data,acc):
		if self.data == data:
			return True
		l=r=False
		if self.data > data:
			if self.left:
				l=self.left.getParentList(data,acc)
		else:
			if self.right:
				r=self.right.getParentList(data,acc)
		if l or r:
			acc.append(self.data)
			return True
		return False

	def getSibling(self,element):
		acc=[False]
		self.getParent(element,acc)
		if acc[0]:
			parentNode = self.search(acc[0])
			if parentNode.left :
				if parentNode.left.data == element:
					if parentNode.right:
						return parentNode.right.data
			else:
				if parentNode.right:
					if parentNode.right.data == element:
						if parentNode.left:
							return parentNode.left.data
		return None

	def checkTree(self,root1,root2):
		if root2 == None and root1 == None:
			return True
		l=not(root2.left !=None and  root1.left==None)
		r=not(root2.right !=None and root1.right == None)
		if l:
			if root2.left != None and root1.left != None: 
				l = self.checkTree(root1.left,root2.left)
		if r:
			if root2.right != None and root1.right != None: 
					r = self.checkTree(root1.right,root2.right)
		return (root1.data == root2.data and l and r)


	def issubtree(self,subrootptr):
		branchroot  = self.search(subrootptr.data)
		if branchroot:
			return self.checkTree(branchroot,subrootptr)
		return False

	def sum(self):
		if not self:
			return 0
		l=r=0
		if self.left:
			l=self.left.sum()
		if self.right:
			r=self.right.sum()
		return self.data+l+r
	

	def minR(self,root):
		if root:
			if root.left:
				return self.minR(root.left)
		return root.data

	def maxl(self,root):
		if root:
			if root.right:
				return self.maxl(root.right)
		return root.data

	def maxLeft(self,root):
		if root:
			if root.left:
				return root.maxl(root.left)
		return False

	def minRight(self,root):
		if root:
			if root.right:
				return self.minR(root.right)
		return False



#--------------------------------------------------------------------


if __name__=="__main__":
	root = BinaraySearchTree(15)
