import random
import numpy as np

def prim(matrix):
	free_nodes = list(matrix.keys())  # Список непосещенных вершин
	start = "s4" # Начальная вершина
	free_nodes.remove(start) # Убираем из непосещенных вершин вершину, с которой начинаем

	visited = [start] # Добавляем в список посещенных вершин вершину, с которой начинаем
	path = [] # Путь остового дерева

	while free_nodes: # Пока не кончатся непосещенные вершины
		distance = float('inf') # Вес ребра между двумя вершинами
		for s in visited: # Перебираем каждую вершину из посещенных
			for d in matrix[s]: # Перебираем каждую вершину
				if d in visited or s == d:  
					continue
				if matrix[s][d] < distance: # Находим ребро с наименьшим весом
					distance = matrix[s][d]
					pre = s
					nxt = d

		path.append((pre, nxt)) # Добавляем в остовое дерево ребро
		visited.append(nxt) # Добавляем вершину в посещенную
		free_nodes.remove(nxt) # Убираем посещенную вершину из непосещенных


	print(path)


def find(node, parent): 
    while parent[node] != node: 
        node = parent[node] 
    return node 
  
def union(i, j, parent): 
    a = find(i, parent) 
    b = find(j, parent) 
    parent[a] = b 
    
def kruskal(matrix, size):
	_ = float('inf')

	parent = [i for i in range(size)]

	mincost = 0  
   
	for i in range(size): 
		parent[i] = i 
  
	node_count = 0
	while node_count < size - 1: 
		min_distance = _ 
		a = -1
		b = -1
		for i in range(size): 
			for j in range(size): 
				if find(i, parent) != find(j, parent) and matrix[i][j] < min_distance: 
					min_distance = matrix[i][j] 
					a = i 
					b = j 
		union(a, b, parent) 
		print('Edge {}:({}, {}) cost:{}'.format(node_count + 1, a + 1, b + 1, min_distance)) 
		node_count += 1
		mincost += min_distance
  
	print("Minimum cost= {}".format(mincost)) 


def get_vertexes(edges):
	vertexes = set()
	for edge in edges:
		vertexes.add(edge[0])
		vertexes.add(edge[1])
	return vertexes


def adjacency_matrix(edges):
	vertexes = get_vertexes(edges)
	
	adjacency_matrix = np.zeros( (len(vertexes), len(vertexes)), dtype = int )

	all_edges_list = []

	for i in range(6):
		for j in range(6):
			if (i + 1, j + 1) in edges:
				all_edges_list.append( (i + 1, j + 1) )

			else:
				all_edges_list.append(0)

	for edge in all_edges_list:
		if edge != 0:
			adjacency_matrix[edge[0] - 1][edge[1] - 1] = 1
			adjacency_matrix[edge[1] - 1][edge[0] - 1] = 1


	return adjacency_matrix


def incidence_matrix(edges):
	vertexes = list(get_vertexes(edges))

	incidence_matrix = np.zeros( (len(vertexes), len(edges) ), dtype = int )

	for i in range(len(vertexes)):
		for j in range(len(edges)):
			if vertexes[i] in edges[j]:
				incidence_matrix[i][j] = 1

	return incidence_matrix

	
