def is_bipartite_dfs(graph, node, colors=None, color=0):
    if colors is None:
        colors = {}
    
    if node in colors:
        return colors[node] == color 
    
    colors[node] = color 
    
    for neighbor in graph[node]:
        
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  
    for node in graph:
        if node not in colors:  
            if not is_bipartite_dfs(graph, node, colors):
                return False  
    return True

def buildgraph(edges):
    nodes = {}
    for a, b in edges:
        if a not in nodes:
            nodes[a] = []
        if b not in nodes:
            nodes[b] = []
        nodes[a].append(b)
    return nodes

n = 4
dislikes = [[1,2],[1,3],[2,4]]

print(check_bipartite(buildgraph(dislikes)))