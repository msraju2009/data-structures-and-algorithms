# -*- coding: UTF-8 -*-

'''
	Program to detect cycle in an undirected graph
'''

# Time-complexity: O(V+E)
class Graph(object):

	def __init__(self, V):
		self.V = V
		self.adj_list = [[] for i in range(self.V)]

	def add_edge(self, src, dest):
		'''Add edge in undirected graph'''
		self.adj_list[src].append(dest)
		self.adj_list[dest].append(src)

	def detect_cycle_util(self, start, parent, visited, rec_stack):
		'''Recursive use depth first search to detect cycle in a graph'''
		if not visited[start]:
			visited[start] = True
			rec_stack[start] = True

			for vertex in self.adj_list[start]:
				if vertex != parent:
					if not visited[vertex] and self.detect_cycle_util(vertex, start, visited, rec_stack):
						return True
					
					elif rec_stack[vertex]:
						return True

		# Remove th current start from recursion stack
		rec_stack[start] = False
		return False

	def detect_cycle(self):
		'''Detect cycle in a undirected graph'''
		visited = [False] * self.V
		rec_stack = [False] * self.V

		for v in range(self.V):
			if self.detect_cycle_util(v, -1, visited, rec_stack):
				return True

		return False

def construct_graph():
	graph = Graph(5)
	graph.add_edge(0, 1)
	graph.add_edge(1, 2)
	graph.add_edge(2, 0)
	graph.add_edge(0, 3)
	graph.add_edge(3, 4)

	return graph

if __name__ == "__main__":
	graph = construct_graph()
	print graph.detect_cycle()
