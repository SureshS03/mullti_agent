from queue import PriorityQueue

# Number of vertices in the graph
v = 14
# Graph represented as an adjacency list
graph = [[] for i in range(v)]

# Function for implementing Best-First Search
# Outputs the path with the lowest cost
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, actual_Src))
    visited[actual_Src] = True

    while not pq.empty():
        u = pq.get()[1]
        
        # Displaying the path with the lowest cost
        print(u, end=" ")
        
        if u == target:
            break
        
        # Explore all neighbors of u
        for v, c in graph[u]:
            if not visited[v]:
                visited[v] = True
                pq.put((c, v))
    
    print()

# Function to add edges to the graph
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# Adding edges with their respective costs
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

# Define source and target nodes
source = 0
target = 9

# Execute the Best-First Search
print("Following is the Best-First Search path:")
best_first_search(source, target, v)
