import sys
class Node(object):

	def __init__(self, data,next=None):
		self.data = data
		self.next = next

class SingleLinkedList():
	
	def __init__(self,limit=-1):
		self.head = None
		self.size = 0
		self.limit = limit
 
	def insert(self,data):
		if self.limit == -1 or self.limit > self.size: 
			self.size += 1 
			if not self.head:
				self.head = Node(data)
			else:
				ptr = self.head
				while ptr.next:
					ptr = ptr.next
				ptr.next = Node(data)
		return self.size


	def insertFirst(self,data):
		self.size+=1
		new_node=Node(data)
		new_node.next = self.head
		self.head = new_node
		return self.size

	def insertBefore(self,data,index):
		if self.limit == -1 or self.limit > self.size: 
			if self.size > index and index!=-1:
				ptr = self.head
				preptr=None
				i=0 
				if index == 0:
					self.insertFirst(data)
				else:
					while ptr:
						if i == index:
							self.size+=1
							new_node = Node(data)
							preptr.next = new_node
							new_node.next = ptr
							return self.size
						i+=1
						preptr=ptr
						ptr = ptr.next
							
	def insertBeforeElement(self,data,referenceElement):
		return self.insertBefore(data,self.linearSearch(referenceElement))

	def deleteHead(self):
		self.size-=1
		n = self.head
		ptr = self.head.next
		self.head = ptr
		return n.data

	def delete(self,element):
		ptr = self.head
		if ptr.data == element :
			self.deleteHead()
		else:
			preptr = None
			while ptr :
				if ptr.data == element :
					self.size-=1
					preptr.next = ptr.next
					break
				preptr=ptr
				ptr = ptr.next


	def linearSearch(self,element):
		ptr = self.head
		index = 0
		while ptr:
			if ptr.data == element:
				return index
			ptr = ptr.next
			index+=1
		return -1


	def minimumValue(self,ptr):
		minValue =sys.maxsize
		minptr = None
		while ptr:
			if minValue > ptr.data:
				minValue = ptr.data
				minptr = ptr
			ptr = ptr.next
		return minptr

	def orderedInsert(self,element):
		ptr = self.head
		while ptr:
			if ptr.data > element:
				self.delete(element)
				self.insertBeforeElement(element,ptr.data)
				break
			ptr = ptr.next

#------------------------------------------------------------------
	def bubbleSort(self):
		ptr = self.head
		postptr = ptr.next
		while ptr:
			while postptr:
				if ptr.data < postptr.data:
					ptr.data , postptr.data =  postptr.data ,ptr.data 
				postptr = postptr.next
			postptr = self.head
			ptr = ptr.next

	def selectionSort(self):
		ptr = self.head
		i = 0
		size = self.size-1
		while i < size:
			mindata = self.minimumValue(ptr)
			ptr.data ,mindata.data = mindata.data , ptr.data  
			i+=1
			ptr = ptr.next

	def insertionSort(self):
		ptr  = self.head
		while ptr:
			self.orderedInsert(ptr.data)
			ptr = ptr.next

	def showList(self):
		array = []
		i=0
		ptr = self.head
		while ptr:
			array.append(ptr.data)
			ptr=ptr.next
		print(array)

#-------------------------------------------------------------------
if __name__ == "__main__":
	bubble = SingleLinkedList()
	for i in range(10,0,-1):
		bubble.insert(i)
	bubble.bubbleSort()
	bubble.showList()

	insertion = SingleLinkedList()
	for i in range(10,0,-1):
		insertion.insert(i)
	insertion.insertionSort()
	insertion.showList()

	selection = SingleLinkedList()
	for i in range(10,0,-1):
		selection.insert(i)
	selection.selectionSort()
	selection.showList()
