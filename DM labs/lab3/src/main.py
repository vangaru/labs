import functions

# ЗАДАНИЕ 1

_ = float('inf')
matrix_dict = {
	"s1":{"s1":_, "s2":5, "s3":8, "s4":_, "s5":11, "s6":_},
	"s2":{"s1":5, "s2":_, "s3":4, "s4":8, "s5":_, "s6":_},
	"s3":{"s1":8, "s2":4, "s3":_, "s4":_, "s5":_, "s6":10},
	"s4":{"s1":_, "s2":8, "s3":_, "s4":_, "s5":6, "s6":2},
	"s5":{"s1":11, "s2":_, "s3":_, "s4":6, "s5":_, "s6":7},
	"s6":{"s1":_, "s2":_, "s3":10, "s4":2, "s5":7, "s6":_}
}

matrix = [
    [_, 5, 8, _, 11, _],
    [5, _, 4, 8, _, _],
    [8, 4, _, _, _, 10],
    [_, 8, _, _, 6, 2],
    [11, _, _, 6, _, 7],
    [_, _, 10, 2, 7, _]
]

#functions.prim(matrix_dict)
#functions.kruskal(matrix, len(matrix))



# ЗАДАНИЕ 2

edges = [(1, 2), (1, 4), (2, 3), (2, 4), (3, 4), (3, 6), (4, 5), (5, 6)]

am = functions.adjacency_matrix(edges)
im = functions.incidence_matrix(edges)

vertexes = functions.get_vertexes(edges)



adjacent_edges = functions.get_adjacent_edges(am)

n = 6
visited = [False] * (n + 1)
prev = [None] * (n + 1)
#functions.get_components(1, visited, prev, adjacent_edges, n)
