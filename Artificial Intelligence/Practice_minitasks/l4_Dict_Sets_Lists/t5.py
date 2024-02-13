# Task no.4 (dictionary representation and run bfs on given graph)
graph = {
    '0': ['1', '2'],
    '1': ['0','2','3','5','6'],
    '2': ['1','3','4','5'],
    '3': ['0','1','2','4'],
    '4': ['3','2','6'],
    '5': ['1','2'],
    '6': ['1','4']
}
visited = []
queue = [] 

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '1')
