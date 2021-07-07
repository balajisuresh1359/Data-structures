from collections import defaultdict

#----------------------------------------------------------------------------
#Graph creation 
class Node():

	def __init__(self, data,next = None):
		self.data = data
		self.next = next
		

def AdjacencyList(num_nodes):
	adjList=[None]*num_nodes
	i=0
	while i<num_nodes:
		print("Enter the number of neighbours of ",i,end=" ")
		n = int(input())
		j=0
		lastNode = None
		while j<n:
			print("Enter the neighbour - %d of node %d"%(j,i),end=" ")
			m = int(input())
			j+=1
			new_node = Node(m)
			if not adjList[i]:
				adjList[i]=new_node
			else:
				lastNode.next = new_node
			lastNode = new_node
		i+=1
	return adjList

def Adjacencymatrix(num_nodes):
	i=0
	Adjacencymatrix =[]
	while i<num_nodes:
		print("Enter the number of neighbours of ",i,end=" ")
		n = int(input())
		j=0
		temp =[]
		while j<n:
			print("Enter the neighbour - %d of node %d"%(j,i),end=" ")
			m = int(input())
			j+=1
			temp.append(m)
		i+=1
		Adjacencymatrix.append(temp)
	return Adjacencymatrix

def dictionaryGraph(num_nodes):
	graph = defaultdict(list)
	i=0
	while i<num_nodes:
		print("Enter the number of neighbours of ",i,end=" ")
		n = int(input())
		j=0
		while j<n:
			print("Enter the neighbour - %d of node %d"%(j,i),end=" ")
			m = int(input())
			j+=1
			graph[i].append(m)
		i+=1
	return graph

#--------------------------------------------------------------------
#Breadth-First-search
def BFS(dictionary,path,start):
	queue=[]
	path.append(start)
	queue.append(start)
	while queue != []:
		node = queue[0]
		del queue[0]
		for i in dictionary.get(node):
			if i not in path:
				queue.append(i)
				path.append(i) 


#Depth-First-search
def DFS(dictionary,path,start):
	stack =[]
	stack.append(start)
	path.append(start)
	while stack!=[]:
		node = stack.pop()
		if node not in path:
			path.append(node)
		for i in dictionary.get(node):
			if i not in path:
				stack.append(i)


#-------------------------------------------------------------------
#Print in normal way

def show_adjlist(adjList,num_nodes):
		i=0
		while i<num_nodes:
			ptr = adjList[i]
			while ptr:
				print(ptr.data,end="--")
				ptr = ptr.next
			print("\n")
			i+=1
def show_adjmat(adjmat):
	for i in adjmat:
	 	print(i)

def show_dictgraph(dictionary):
	for i in dictionary:
		print(dictionary.get(i))

#-------------------------------------------------------------------------------

if __name__ == "__main__":
	pass
