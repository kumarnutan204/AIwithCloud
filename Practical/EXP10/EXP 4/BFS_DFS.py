graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

#to strore the bfs visited nodes from bfs
visited_bfs = []
queue = []

def bfs(visited_bfs, graph, node):
  visited_bfs.append(node)
  queue.append(node)
    #queue is used in order to explore all the queues on that node
  while queue:
    s = queue.pop(0) 
    print (s, end = "->") 

    for neighbour in graph[s]:
      if neighbour not in visited_bfs:
        visited_bfs.append(neighbour)
        queue.append(neighbour)

#using a set to store the visited nodes
visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print (node, end="->")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("BFS order of visiting the nodes:" , end =" ")
bfs(visited_bfs, graph, 'A')
print('\n')
print("DFS order of visiting the nodes:" , end =" ")
dfs(visited, graph, 'A')