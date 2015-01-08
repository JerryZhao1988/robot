#!/usr/bin/python
import fileinput, sys

# 	I used a* algorithm to solve this problem
# 	The main idea is f(x) = g(x) + h(x)

class a_star(object):

# 	I used three matrixs to store the infomation 
# 	matrix is the given map by stdin
# 	path_matrix stored how the best parent visit the child node, just need to store :u d l r
# 	f_matrix stored the f value of every node which is in open_queue
# 	open_queue and close_queue are parts of the algorithm

#	when create a object, it would build the map and empty matrixs then chose a suitable weight 
#	for h function 
	def __init__(self,filepath):
		self.matrix = []
		self.open_queue=[]
		self.close_queue=[]
		self.readmap(filepath)
		self.x_end = len(self.matrix[0])
		self.y_end = len(self.matrix)
		self.f_matrix = [[0 for i in xrange(self.x_end)] for i in xrange(self.y_end)]
		self.path_matrix = [["" for i in xrange(self.x_end)] for i in xrange(self.y_end)]
		self.weight = (int(self.matrix[0][0], 16) + 
			int(self.matrix[self.y_end-1][self.x_end-1], 16))/2

#	This function set the startpoint,endpoint and set s mark in path matrix
	def set_point(self, startpoint, endpoint):
		for (a,b) in [startpoint,endpoint]:
			if a < 0 or b < 0:
				return False

		self.startpoint = startpoint
		self.endpoint = endpoint
		self.setvalue(startpoint,0,"s")
		return True

#	Just the h(x) function, i used edit distance  d = (x-x') + (y-y')
	def h(self,x,y):
		return (abs(self.endpoint[0] - x) + abs(self.endpoint[1] - y))/2 * self.weight

#	readmap
	def readmap(self,filepath):
		in_file = open(filepath,"r")
		for line in in_file.readlines():
			if not line.strip():
				continue
			Nodes =line.split()
			self.matrix.append(Nodes)
		in_file.close()
		return True

#	It compare the value of f(x) and update the minimal path and value, 
#	and also insert the checked point into open_queue 
	def setvalue(self,point,va,navi):
		if self.f_matrix[point[1]][point[0]] == 0 or self.f_matrix[point[1]][point[0]][1] >= va+int(self.matrix[point[1]][point[0]], 16) + self.h(point[0],point[1]):
			self.f_matrix[point[1]][point[0]] = (point,va+int(self.matrix[point[1]][point[0]], 16) + self.h(point[0],point[1]))
			self.path_matrix[point[1]][point[0]] = navi
			if point not in self.open_queue:
				self.open_queue.append(point)
			return True
		return False

# 	When give a point, it would visit its neighboors 
#	As f(x) = g(x) + h(x), so g(x) = f(x) - h(x)
#	g(x) is the actully cost
	def viewpoint(self,x,y):
		if x !=0:
			if (x-1,y) not in self.close_queue:
				self.setvalue((x-1,y),self.f_matrix[y][x][1]-self.h(x,y),"l")

		if y != 0:
			if (x,y-1) not in self.close_queue:
				self.setvalue((x,y-1),self.f_matrix[y][x][1]-self.h(x,y),"u")

		if x != self.x_end-1:
			if (x+1,y) not in self.close_queue:
				self.setvalue((x+1,y),self.f_matrix[y][x][1]-self.h(x,y),"r")

		if y != self.y_end-1:
			if (x,y+1) not in self.close_queue:
				self.setvalue((x,y+1),self.f_matrix[y][x][1]-self.h(x,y),"d")
		return True

#	This function should be written in heap and use heapsort to get the minimal value point
# 	I just write a simple way to get the minimal point 		
	def findminipoint(self):
		f = []
		mini = 0
		point = ()
		for i in self.f_matrix:
			L = filter(None, i)
			f += L
		for (a,b) in f:
			if mini == 0 :
				mini = b
			if b <=  mini:
				point = a
		return point

#	It starts at endpoint and travel to startpoint and records the path 
	def get_path(self):
		path = []
		(x,y)=self.endpoint
		while (x,y) != self.startpoint:
			path.append(self.path_matrix[y][x])
			if self.path_matrix[y][x] == "u":
				y += 1
			elif self.path_matrix[y][x] == "d":
				y -= 1
			elif self.path_matrix[y][x] == "l":
				x += 1
			elif self.path_matrix[y][x] == "r":
				x -= 1
		return path[::-1]

#	It would keep searching the path in open_queue until no node in open_queue
#	When a node is visited, it would be put in close_queue, means it has found the best path to itself
	def running(self):
		find = True
		while self.open_queue != None:
			if self.endpoint in self.close_queue:
				break
			(x,y)=self.findminipoint()
			self.viewpoint(x,y)
			# print self.open_queue
			self.open_queue.remove((x,y))
			self.close_queue.append((x,y))
			self.f_matrix[y][x] = 0
		else:
			find = False
			return "Can not find a path to endpoint"
		if find:
			return self.get_path()

def main():
	test = a_star(sys.argv[1])
	if len(sys.argv) > 2:
		startpoint = (int(sys.argv[2]),int(sys.argv[3]))
		endpoint =	(int(sys.argv[4]),int(sys.argv[5]))
	else:
		startpoint = (0,0)
		endpoint = (5,5) 

	test.set_point(startpoint,endpoint)
	print test.running()

if __name__ == "__main__":
	main()

# I used A* algorithm, because it is a widely used pathfinding algorithm and it 
# use a knowledge-plus-heuristic cost function to improve the searching speed.
# Compared with Dijkstra and DFS, it saved a lot time by cutting the costly path.

# The time complexity of it is depends on how the map is consisted and the heuristic
# function, so does the sapce complexity.
# In worst case, it would store all the node's infomation, and search every node in graph.
# Generally, the time complexity is O(log h'(x)) 







