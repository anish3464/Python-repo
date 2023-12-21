def dfs(node, visited, graph, current_length):
    visited[node] = True
    max_length = current_length
    for neighbor, edge_length in graph[node]:
        if not visited[neighbor]:
            max_length = max(max_length, dfs(neighbor, visited, graph, current_length + edge_length))
    visited[node] = False 
    return max_length

def find_maximum_total_length(N, roads):
    graph = [[] for _ in range(N + 1)]
    for A, B, C in roads:
        graph[A].append((B, C))
        graph[B].append((A, C))
    max_total_length = 0
    for start_node in range(1, N + 1):
        visited = [False] * (N + 1)
        max_total_length = max(max_total_length, dfs(start_node, visited, graph, 0))
    return max_total_length

n,m=map(int,input().split())
roads=[]
for i in range(m):
    l=list(map(int,input().split()))
    roads.append(l)
print(find_maximum_total_length(n, roads))  
