cities = input().split()

def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()
        
        if start not in visited:
            visited.add(start)
            if start in graph:
                for neigh in graph[start]:
                    dfs(graph, neigh, visited)
        return visited
    
def buildgraph(lst):
    graph = {}
    stsah = {}
    stvih = {}
    nodes = set()
    for i in lst:
        if i[0] not in graph:
            graph[i[0]] = []
        if i[-1] not in graph:
            graph[i[-1]] = []
        graph[i[0]].append(i[-1])
        
        stvih[i[0]] = stvih.get(i[0], 0)+1
        stsah[i[-1]] = stsah.get(i[-1], 0)+1
        nodes.update([i[0], i[-1]])
        
    start_nodes = sum(1 for node in nodes if stvih.get(node, 0) - stsah.get(node, 0) == 1)
    end_nodes = sum(1 for node in nodes if stsah.get(node, 0) - stvih.get(node, 0) == 1)
    
    if not (start_nodes in [0, 1] and end_nodes in [0, 1]):
        return False
    
    fnode = list(graph.keys())[0]
    visited = set()
    dfs(graph,fnode)
    
    if len(dfs(graph,fnode)) != len(graph):
        return False
    
    return True

print(buildgraph(cities))