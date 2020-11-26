
V = 7

INF  = 99999
  
def floydWarshall(graph): 
  
    dist = list(map(lambda i : list(map(lambda j : j , i)) , graph)) 
      
    for k in range(V): 
        for i in range(V): 
            for j in range(V): 
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j]) 
                                 
    printSolution(dist) 
  
  

def printSolution(dist): 
    print ("Following matrix shows the shortest distancesbetween every pair of vertices") 
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%7s" %("INF")) 
            else: 
                print ("%7d\t" %(dist[i][j])) 
            if j == V-1: 
                print ("") 
  
  
  

graph = [[INF, 10, INF, 8, INF, INF, INF],
          [INF, INF, 7, INF, INF, INF, INF],
          [INF, INF, INF, 11, 5, 6, INF],
          [INF, INF, INF, INF, 8, INF, INF],
          [INF, INF, INF, INF, INF, 4, INF],
          [INF, INF, INF, INF, INF, INF, 9],
          [INF, INF, INF, INF, INF, INF, INF]]

floydWarshall(graph); 
