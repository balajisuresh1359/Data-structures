class Node:

	def __init__(self, data,next=None):
		super(Node, self).__init__()
		self.data = data
		self.next = next
    
class LinkedList:
	
  def __init__(self):
		self.head=None
	
  def insertBefore(self,data):
		newNode=Node(data)
		newNode.next=self.head
		self.head=newNode
	
  def insertAfter(self,data):
		newNode=Node(data)
		if self.head == None :
			self.head = newNode
		else:
			itr=self.head
			while itr.next:
				itr=itr.next
			itr.next=newNode
	
  def removeByindex(self,index):
		if index >= self.getLength() or index < 0  :
			return print("Invalid index/index out of bound..!!!")
		ptr=self.head
		postptr=ptr.next
		i=0
		while i!=index-1:
			ptr=ptr.next
			postptr=ptr.next
			i+=1
		ptr.next=postptr.next

	def removeByvalue(self,data):
		ptr=self.head
		postptr=ptr.next
		while ptr:
			if ptr.data == data :
				ptr.next=postptr.next
				return
			ptr=ptr.next
			postptr=ptr.next
		return print("not found")

	def display(self):
		itr=self.head
		items=""
		while itr:
			items+=str(itr.data)
			items+='->'
			itr=itr.next
		return items[0:len(items)-2]
	
  def getLength(self):
		i=self.head
		while i:
			self.count+=1
			i=i.next
		return self.count
