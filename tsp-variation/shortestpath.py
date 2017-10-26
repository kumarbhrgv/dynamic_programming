import copy
from collections import defaultdict
class Graph:

	def __init__(self,vertices):
		self.vertices= vertices 
		self.graph = defaultdict(list)
		self.costofEdge = defaultdict(list)
		self.path_list = []
		self.path_to_cost={}
		self.min = -1
		self.cost_to_home = []

	#Edge u to v with cost = c
	def addEdge(self,u,v,cost=1):
		self.graph[u].append(v)
		if u in self.costofEdge.keys():
			if v in self.costofEdge[u].keys():
				self.costofEdge[u][v]=cost
			else:
				inner_dict = self.costofEdge[u]
				inner_dict[v] = cost
				self.costofEdge[u] = (inner_dict)
		else:
			inner_dict = {}
			inner_dict[v] = cost
			self.costofEdge[u] = inner_dict
	
	#remove the discount from all the edges that have indegree not 0 
	#for a given vertex v
	def addDiscount(self,vertex,discount):
		if vertex == 0:
			return
		for i in self.costofEdge:
			if vertex in self.costofEdge[i].keys():
				self.costofEdge[i][vertex]-=discount
	
	
	def printresults(self):
		print("all possible paths:",self.path_list)
		self.min = list(self.path_to_cost.values())[0]
		min_path=[]
		for i in range(len(self.path_list)):
			if self.min > self.path_to_cost[i]:
				min_path = self.path_list[i]
				self.min = self.path_to_cost[i]
		print("minimum cost:",self.min,min_path)

	#DFS to find all possible paths from node u to d 
	#visted array for all s to d
	def compute_all_paths(self, u, d, visited, path):		
		visited[u]= True
		path.append(u)
		if u ==d:
			cost =0
			path_copy = copy.deepcopy(path)
			path_copy.append(0)
			for i in range(len(path_copy) -1):
				j = i+1
				cost += self.costofEdge[path_copy[i]][path_copy[j]]
			self.path_to_cost[len(self.path_list)] = cost
			self.path_list.append(path_copy)
			print(path_copy,cost)
		else:
			for i in self.graph[u]:
				if visited[i]==False:
					self.compute_all_paths(i, d, visited, path)
		path.pop()
		visited[u]= False

	#DFS on start to destination
	def dfs(self,s, d):
		visited =[False]*(self.vertices)
		path = []
		self.compute_all_paths(s, d,visited, path)

g = Graph(3)
#Assuming that cost from same node is not needed,commenting below lines
#g.addEdge(0,0,0)
#g.addEdge(2,2,0)
#g.addEdge(1,1,0)

#[0,1 = 5]
g.addEdge(0,1,5)
#[0,2 = 6]
g.addEdge(0,2,6)
#[1,0 = 5]
g.addEdge(1,0,5)
#[2,0 = 6]
g.addEdge(2,0,6)
#[1,2 = 1]
g.addEdge(1,2,1)
#[2,1 = 30]
g.addEdge(2,1,30)

#Discount/Reward on 1 is 1 and reward on 2 is 3.

g.addDiscount(1,1)
g.addDiscount(2,3)


s = 0 ;
mall_array = [1,2]
for i in mall_array :
	print("Following are all different paths from %d through %d :" %(s, i))
	#for all nodes in graph other than home do dfs to find all possible paths
	g.dfs(s, i)
g.printresults()
