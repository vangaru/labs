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

def get_all_edges_list(edges, vertexes):
	all_edges_list = []

	for i in range(len(vertexes)):
		for j in range(len(vertexes)):
			if (i + 1, j + 1) in edges:
				all_edges_list.append( (i + 1, j + 1) )

			else:
				all_edges_list.append( () )

	return all_edges_list


def adjacency_matrix(edges):
	vertexes = get_vertexes(edges)
	
	adjacency_matrix = np.zeros( (len(vertexes), len(vertexes)), dtype = int )

	all_edges_list = get_all_edges_list(edges, vertexes)


	for edge in all_edges_list:
		if len(edge) == 2:
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


def get_vertex_power(vertex, incidence_matrix):
	vertex_edges = incidence_matrix[vertex - 1]
	power = 0
	for edge in vertex_edges:
		if edge == 1:
			power += 1
	return power

def print_vertexes_power(vertexes, incidence_matrix):
	for vertex in vertexes:
		power = get_vertex_power(vertex, incidence_matrix)
		print("Вершина: " + str(vertex) + " Мощность: " + str(power)) 
	


# ПОИСК В ГЛУБИНУ

def get_adjacent_edges(matrix):
	adjacent_edges = dict()
	for i in range(len(matrix)):
		edges = set()
		for j in range(len(matrix)):
			if matrix[i][j] == 1:
				edges.add(j + 1)
		adjacent_edges[i + 1] = edges
	return adjacent_edges

def dfs(start, visited, prev, adjacent_edges):
    visited[start] = True
    for i in adjacent_edges[start]:
        if not visited[i]:
            prev[i] = start 
            dfs(i, visited, prev, adjacent_edges)

def get_components(start, visited, prev, adjacent_edges, n):
	ncomp = 0
	for i in range(1, n + 1):
		if not visited[i]:
			ncomp += 1
			dfs(i, visited, prev, adjacent_edges)
	print("Количество компонент связности: " + str(ncomp))

#ПОИСК В ШИРИНУ
