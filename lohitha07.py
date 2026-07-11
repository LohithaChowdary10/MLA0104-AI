from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                queue.append(neighbour)

    return visited


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in reversed(graph[node]):
                stack.append(neighbour)

    return visited


graph = {}

n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (Parent Child): ").split()

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)

start = input("Enter starting node: ")

print("BFS:", bfs(graph, start))
print("DFS:", dfs(graph, start))
