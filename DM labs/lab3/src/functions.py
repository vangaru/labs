import random

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
  
	edge_count = 0
	while edge_count < size - 1: 
		min = _ 
		a = -1
		b = -1
		for i in range(size): 
			for j in range(size): 
				if find(i, parent) != find(j, parent) and matrix[i][j] < min: 
					min = matrix[i][j] 
					a = i 
					b = j 
		union(a, b, parent) 
		print('Edge {}:({}, {}) cost:{}'.format(edge_count + 1, a + 1, b + 1, min)) 
		edge_count += 1
		mincost += min
  
	print("Minimum cost= {}".format(mincost)) 


