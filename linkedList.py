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

	def insertAfter(self,data,index):
		if (self.limit == -1 or self.limit > self.size) and index!=-1:  
			if self.size-1 == index :
				self.insert(data)
			elif self.size >= index:
				ptr = self.head
				postptr = ptr.next
				i=0
				while postptr:
					if i == index:
						new_node = Node(data)
						ptr.next = new_node
						new_node.next = postptr
						self.size+=1
						return self.size
					i+=1
					ptr = ptr.next
					postptr = ptr.next
			else:
				return None
 
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
							

	def insertAfterElement(self,data,referenceElement):
		return self.insertAfter(data,self.linearSearch(referenceElement))

	def insertBeforeElement(self,data,referenceElement):
		return self.insertBefore(data,self.linearSearch(referenceElement))

	def insertFirst(self,data):
		self.size+=1
		new_node=Node(data)
		new_node.next = self.head
		self.head = new_node
		return self.size

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

	def deleteAfter(self,index):
		if (self.limit == -1 or self.limit > self.size) and index!=-1:  
			if index < self.size:
				ptr = self.head
				postptr = ptr.next
				i=0
				while postptr:
					if i == index:
						ptr.next = postptr.next
						self.size-=1
						return postptr.data
					i+=1
					ptr = ptr.next
					postptr = ptr.next


	def deleteBefore(self,index):
		if self.limit == -1 or self.limit > self.size: 
			if self.size > index and index > 0 :
				if index == 1:
					self.deleteHead()
				else:
					ptr = self.head
					preptr =None
					i=0
					while ptr:
						if i == index-1:
							preptr.next = ptr.next
							self.size-=1
							return ptr.next
						i+=1
						preptr = ptr
						ptr = ptr.next
					
	def deleteAfterElement(self,referenceElement):
		return self.deleteAfter(self.linearSearch(referenceElement))

	def deleteBeforeElement(self,referenceElement):
		return self.deleteBefore(self.linearSearch(referenceElement))


	def linearSearch(self,element):
		ptr = self.head
		index = 0
		while ptr:
			if ptr.data == element:
				return index
			ptr = ptr.next
			index+=1
		return -1

	def swapOptional(self,element_1,element_2):   #elemnet may not present 
		index_1 = self.linearSearch(element_1)
		index_2 = self.linearSearch(element_2)
		if index_2!=-1 and index_1!=-1 :
			ptr = self.head
			i=count=0
			while (i <= index_1) or (i <= index_2):
				if i == index_1 :
					ptr.data = element_2
				if i == index_2 :
					ptr.data = element_1
				i+=1
				ptr = ptr.next

	def getElement(self,index):
		ptr = self.head
		i=0
		if index < self.size :
			while ptr:
				if index == i:
					return ptr.data
				i+=1
				ptr = ptr.next

	def swap(self,element_1,element_2):  
		ptr = self.head
		count = 0
		flag1 =1
		flag2 =1
		while ptr:
			if ptr.data == element_1 and flag1:
				ptr.data = element_2
				ptr = ptr.next
				flag1 =0
				count+=1
			if ptr.data == element_2 and flag2:
				ptr.data = element_1
				ptr = ptr.next
				flag2 =0
				count+=1
			if count == 2:
				break
			ptr = ptr.next

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

	def insertionSort(self):
		ptr  = self.head
		while ptr:
			self.orderedInsert(ptr.data)
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

	def reversedList(self):
		ptr = self.head
		preptr =None
		while ptr:
			next_ptr = ptr.next 
			ptr.next = preptr
			preptr = ptr
			ptr = next_ptr
		self.head = preptr


	def getlenght(self):
		ptr = self.head
		count = 0
		while ptr :
			ptr.next = ptr
			count+=1
		self.size = count
		return count

	def linkedListToarray(self):
		array = []
		ptr = self.head
		while ptr:
			array.append(ptr.data)
		return array

	def arrayTolinkedlist(self,array):
		for i in array:
			self.insert(i)
		return self.head
			
	def pop(self):
		return self.deleteAfter(self.size-2)

	def push(self,data):
		return self.insert(data)

	def shift(self):
		return self.deleteHead()

	def unshift(self,data):
		return self.insertFirst(data)

	def sum(self):
		s =0
		ptr = self.head
		while ptr:
			s+=ptr.data
			ptr = ptr.next
		return s

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
	array = SingleLinkedList()
