graph = {
    'A':['B','G'], 
    'B':['A','F','C'],
    'C':['B','D','F'],
    'D':['E'],
    'E':[],
    'F':['B','C','H'],
    'G':['A','H'],
    'H':['G','F'],
}

visitedDFS=set()
def DFS(visitedDFS,graph,root):
    if root not in visitedDFS:
        print(root)
        visitedDFS.add(root)
        for neighbour in graph[root]:
            DFS(visitedDFS,graph,neighbour)
            

DFS(visitedDFS,graph,'A')


visitedBFS=[]
queue=[]
def BFS(visitedBFS,graph,root):
    visitedBFS.append(root)
    queue.append(root)
    
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        
        for neighbour in graph[m]:
            if neighbour not in visitedBFS:
                visitedBFS.append(neighbour)
                queue.append(neighbour)
                
                
BFS(visitedBFS,graph,'A')
                