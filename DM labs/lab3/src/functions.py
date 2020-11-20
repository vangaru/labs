import random

def prim(matrix):
	free_nodes = list(matrix.keys())  # Список непосещенных вершин
	start = random.choice(free_nodes) # Начальная вершина
	free_nodes.remove(start) # Убираем из непосещенных вершин вершину, с которой начинаем

	visited = [start] # Добавляем в список посещенных вершин вершину, с которой начинаем
	path = [] # Путь остового дерева
	overall_distance = 0 # Сумма весов всех ребер остового дерева

	while free_nodes: # Пока не кончатся непосещенные вершины
		distance = float('inf') # Вес ребра между двумя вершинами
		for s in visited: # Перебираем каждую вершину из посещенных
			for d in matrix[s]: # Перебираем каждую вершину
				if d in visited or s == d or d == 0:  
					continue
				if matrix[s][d] < distance: # Находим ребро с наименьшим весом
					distance = matrix[s][d]
					pre = s
					nxt = d
					overall_distance += distance

		path.append((pre, nxt)) # Добавляем в остовое дерево ребро
		visited.append(nxt) # Добавляем вершину в посещенную
		free_nodes.remove(nxt) # Убираем посещенную вершину из непосещенных


	print(path)
	print("distance = " + str(overall_distance))


