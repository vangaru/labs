
def find(node): 
    while parent[node] != node: 
        node = parent[node] 
    return node 
  
def union(i, j): 
    a = find(i) 
    b = find(j) 
    parent[a] = b 
    
def kruskalMST(matrix, size): 
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
                if find(i) != find(j) and matrix[i][j] < min: 
                    min = matrix[i][j] 
                    a = i 
                    b = j 
        union(a, b) 
        print('Edge {}:({}, {}) cost:{}'.format(edge_count + 1, a + 1, b + 1, min)) 
        edge_count += 1
        mincost += min
  
    print("Minimum cost= {}".format(mincost)) 

V = 6
parent = [i for i in range(V)] 
_ = float('inf') 
matrix = [
    [_, 5, 8, _, 11, _],
    [5, _, 4, 8, _, _],
    [8, 4, _, _, _, 10],
    [_, 8, _, _, 6, 2],
    [11, _, _, 6, _, 7],
    [_, _, 10, 2, 7, _]
]
  
  
kruskalMST(matrix, V)