from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

# Example graph represented as an adjacency List
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Starting node for BFS
start_node = 'A'

print("BFS Traversal:")
bfs(graph,start_node)   