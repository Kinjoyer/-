def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    if start not in visited:
        visited.add(start)
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)
    return visited

def buildgraph(edges):
    nodes = {}
    for a, b in edges:
        if a not in nodes:
            nodes[a] = []
        if b not in nodes:
            nodes[b] = []
        nodes[a].append(b)
    return nodes

n = 8
edges = [[0,3], [0,4], [1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]


edgesl = buildgraph([list(edge[::-1]) for edge in edges])

otv = []

for i in range(n):
    otv.append(list(dfs(edgesl, i)))
    otv[i].pop()

print(otv)
    

