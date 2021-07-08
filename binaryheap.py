#Max heap
import sys
class Heap:						

	def __init__(self,size):
		self.heap = [None]*size   #initialize the heap array
		self.size =size
		self.heapsize=1   #1 based index

	def percolateUp(self,i):
		parent = i//2			#Compute parent index
		if i<=0 or parent<=0:	#Check whether array out of bound 
			return None
		if self.heap[parent] < self.heap[i]:  										#Check whether parent is smaller than child or not
			self.swap(parent,i)
			self.percolateUp(parent)												#For recursively adjust the heap

	def percolateDown(self,i):
		leftchild = (2*i)						#Compute left child
		if leftchild >= self.heapsize:  		#Out of bound condition
			return None
		rightchild = (2*i)+1					#Compute right child
		if self.heap[rightchild] == None:		#if right child is None/empty/last befor element ,then simply swap 
			if self.heap[i] < self.heap[leftchild]:
				self.swap(leftchild,i)
			return None
		else:
			index=leftchild
			if self.heap[index] < self.heap[rightchild]:  #Finding largest child element
				index = rightchild
			if self.heap[index] > self.heap[i]:			  #if parent smaller than child,then swap 
				self.swap(index,i)			
				self.percolateDown(index)				 #For recursively adjust the heap


	def push(self,data):
		if self.heapsize >= self.size: 
			return print("Heap overflow!!!!!...")
		self.heap[self.heapsize] = data
		self.heapsize+=1
		self.percolateUp(self.heapsize-1)

	def pop(self):
		if self.heapsize == 0:
			return print("Heap underflow!!!!!...")
		poppedElement = self.heap[1]
		self.heap[1]  = self.heap[self.heapsize-1]  #Place the smallest element in the first/root position .
		self.heap[self.heapsize-1] = None           #Erase/Remove the smallest element from it previous position .
		self.heapsize-=1
		self.percolateDown(1)
		return poppedElement

	def maxheap_To_minheap(self,i):
		leftchild = 2*i
		rightchild= (2*i)+1
		if leftchild >=self.heapsize:
			return None
		if self.heap[rightchild] == None:
			self.swap(leftchild,i)
			return None
		index = leftchild
		if self.heap[index] > self.heap[rightchild]:
			index = rightchild
		self.swap(index,i)
		self.maxheap_To_minheap(leftchild)
		self.maxheap_To_minheap(rightchild)

	def search(self,data,i):
		
		if i >= self.heapsize or self.heap[i] == None:
			return 0
		if self.heap[i] == data:
			return i
		leftchild = self.search(data,(2*i))  #Check left subtree first 
		if not leftchild:
			return self.search(data,(2*i))+self.search(data,((2*i)+1))
		return leftchild

	def getMin(self,i):
		if i >= self.heapsize:
			return sys.maxsize
		leftchild = 2*i
		rightchild=(2*i)+1
		if leftchild >= self.heapsize:   #Condition for leaf node
				return self.heap[i]
		return min(self.getMin(leftchild),self.getMin(rightchild))

	def getMax(self):
		return self.heap[1]

	def swap(self,i,j):
		self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i] 

	def Kth_largest(self,k):
		if k < self.heapsize:
			i=1
			poppedElements=[]
			while i != k+1:
				j = self.pop()
				poppedElements.append(j)
				i+=1
			while poppedElements!=[]:
				self.push(poppedElements.pop())
			return j

	def heapsort(self):
		n=self.heapsize-1
		for i in range(1,n):
			self.swap(1,self.heapsize-1)
			self.heapsize-=1
			self.percolateDown(1)
		self.heapsize = n+1

	def show(self):
		for i in range(1,self.heapsize):
			print(self.heap[i],end=" ")
		print("\n")


#-----------------------------------------------------------
if __name__ == "__main__":
	heap = Heap(7)
